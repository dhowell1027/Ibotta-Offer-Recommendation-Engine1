from fastapi import FastAPI
from app.models.prediction import predict_offer_redemption
from app.models.recommendation import get_recommendations

app = FastAPI()

# Root endpoint to test the app is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Ibotta Offer Recommendation Engine"}

# Endpoint to get recommendations for a user
@app.get("/recommendations/{user_id}")
def recommendations(user_id: int):
    recommendations = get_recommendations(user_id)
    return {"user_id": user_id, "recommendations": recommendations}

# Endpoint to predict offer redemption for a specific user and offer
@app.get("/predict_redemption/{user_id}/{offer_id}")
def predict_redemption(user_id: int, offer_id: int):
    prediction = predict_offer_redemption(user_id, offer_id)
    return {"user_id": user_id, "offer_id": offer_id, "redemption_probability": prediction}
