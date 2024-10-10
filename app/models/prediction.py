from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Function to train a mock prediction model (this should ideally be done in a separate training script)
def train_offer_prediction_model():
    # Load example data (you should replace this with your actual data)
    user_data = pd.read_csv('data/cleaned_orders.csv')

    # Example features: number of past purchases and time of day of the order
    user_data['num_purchases'] = user_data.groupby('user_id')['order_id'].transform('count')
    user_data['is_morning'] = user_data['order_hour_of_day'].apply(lambda x: 1 if 5 <= x <= 11 else 0)

    # Creating a mock target variable 'offer_redeemed' (replace this with actual labels)
    user_data['offer_redeemed'] = user_data['num_purchases'].apply(lambda x: 1 if x > 10 else 0)

    # Features and target variable
    X = user_data[['num_purchases', 'is_morning']]
    y = user_data['offer_redeemed']

    # Train a simple RandomForestClassifier model
    model = RandomForestClassifier()
    model.fit(X, y)

    return model

# Function to predict if the offer will be redeemed by the user
def predict_offer_redemption(user_data):
    # Mock training of the model (in real applications, load a pre-trained model)
    model = train_offer_prediction_model()

    # Extract features from the user_data
    num_purchases = user_data.features['purchase_history']
    is_morning = 1 if user_data.features['time_of_day'] == 'morning' else 0

    # Prepare the data for prediction
    X_predict = [[num_purchases, is_morning]]

    # Predict if the offer will be redeemed
    prediction = model.predict(X_predict)

    return bool(prediction[0])
