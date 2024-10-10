from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import File, UploadFile
from pydantic import BaseModel
import subprocess
import os

from app.models.recommendation import recommend_offers
from app.models.prediction import predict_offer_redemption

app = FastAPI()

# Set the path to the templates directory
templates = Jinja2Templates(directory="templates")

# Directory to store datasets
DATA_DIR = "data"
COMPETITION_NAME = "instacart-market-basket-analysis"

# UserData model for predictions
class UserData(BaseModel):
    user_id: int
    offer_id: int
    features: dict  # Contains 'purchase_history' and 'time_of_day'

# Event to download the data from Kaggle during FastAPI startup
@app.on_event("startup")
async def download_data():
    """Download dataset from Kaggle during FastAPI startup."""
    
    # Check if the data directory exists, if not, create it
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Check if the dataset has already been downloaded
    if not os.path.exists(f'{DATA_DIR}/orders.csv'):
        # Run the Kaggle command to download the dataset
        kaggle_download_command = f'kaggle competitions download -c {COMPETITION_NAME} -p {DATA_DIR}'
        unzip_command = f'unzip {DATA_DIR}/{COMPETITION_NAME}.zip -d {DATA_DIR}'
        
        # Download the dataset
        print("Downloading dataset from Kaggle...")
        subprocess.run(kaggle_download_command, shell=True)
        
        # Unzip the dataset
        print("Unzipping the dataset...")
        subprocess.run(unzip_command, shell=True)
    
    print("Dataset is ready for use.")

# Root endpoint for the homepage
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "recommendations": []})

# Endpoint for recommending offers
@app.get("/recommend", response_class=HTMLResponse)
async def recommend(request: Request, user_id: int):
    recommendations = recommend_offers(user_id)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "recommendations": recommendations
    })

# Endpoint for predicting if a user will redeem an offer
@app.post("/predict/")
async def predict_offer_redemption_route(user_data: UserData):
    prediction = predict_offer_redemption(user_data)
    return {"offer_redeemed": prediction}

# Optional file upload feature
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    """Allows users to upload a custom dataset."""
    
    # Save the uploaded file to the data directory
    file_location = f"{DATA_DIR}/{file.filename}"
    with open(file_location, "wb+") as buffer:
        buffer.write(file.file.read())
    
    return {"filename": file.filename, "message": "File uploaded successfully!"}
