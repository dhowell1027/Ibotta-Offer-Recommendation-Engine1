import pandas as pd
import joblib
import os

# Path to the trained model
MODEL_PATH = "models/offer_redemption_model.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Please train the model first.")
    
    model = joblib.load(MODEL_PATH)
    return model

# Function to predict offer redemption probability
def predict_offer_redemption(user_id: int, offer_id: int):
    model = load_model()
    
    # Simulate loading user features (e.g., past purchases)
    user_features = get_user_features(user_id)
    offer_features = get_offer_features(offer_id)
    
    # Combine user and offer features for prediction input
    features = combine_user_and_offer_features(user_features, offer_features)
    
    # Predict the redemption probability
    redemption_probability = model.predict_proba([features])[0][1]  # Probability of class 1 (redemption)
    
    return redemption_probability

# Example function to retrieve user features (in practice, use real data)
def get_user_features(user_id):
    # Placeholder: Returning some dummy features based on user_id
    return {
        'purchase_count': 10,
        'loyalty_score': 0.8,
    }

# Example function to retrieve offer features
def get_offer_features(offer_id):
    return {
        'offer_discount': 0.15,
        'offer_category': 1,  # Could be one-hot encoded categories
    }

# Combine user and offer features into a single feature vector
def combine_user_and_offer_features(user_features, offer_features):
    combined_features = [
        user_features['purchase_count'],
        user_features['loyalty_score'],
        offer_features['offer_discount'],
        offer_features['offer_category']
    ]
    return combined_features
