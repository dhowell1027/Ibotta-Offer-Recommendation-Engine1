from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.models.recommendation import recommend_offers, visualize_user_purchases
from app.models.prediction import predict_offer_redemption

# Initialize FastAPI application
app = FastAPI()

# Initialize Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Data model for user input
class UserData(BaseModel):
    user_id: int
    offer_id: int
    features: dict  # Contains features like 'purchase_history', 'time_of_day', etc.

# Root endpoint for the homepage with the recommendation form
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "recommendations": []})

# Endpoint to recommend offers for a specific user based on their ID
@app.get("/recommend", response_class=HTMLResponse)
async def recommend(request: Request, user_id: int):
    # Get recommendations for the user
    recommendations = recommend_offers(user_id)
    
    # Generate a plot visualizing the user's purchase history
    plot_path = visualize_user_purchases(user_id)
    
    # Render the results on the HTML page
    return templates.TemplateResponse("index.html", {
        "request": request,
        "recommendations": recommendations,
        "plot_path": plot_path
    })

# Endpoint to predict if a user will redeem an offer based on their data
@app.post("/predict/")
async def predict_offer_redemption_route(user_data: UserData):
    # Get prediction (True/False) on whether the user will redeem the offer
    prediction = predict_offer_redemption(user_data)
    
    # Return the prediction in JSON format
    return {"offer_redeemed": prediction}
