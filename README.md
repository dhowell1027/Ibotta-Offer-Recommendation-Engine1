Ibotta Offer Recommendation Engine
Overview

The Ibotta Offer Recommendation Engine is a machine learning project that provides personalized product recommendations and predicts whether a user is likely to redeem an offer. It uses data such as past purchase behavior to generate recommendations and predictive models to estimate offer redemption probabilities. The application is built using FastAPI for the backend, pandas for data processing, and scikit-learn for the predictive model.
Features

    Personalized Offer Recommendations: Recommends offers based on a user's purchase history.
    Offer Redemption Prediction: Predicts if a user is likely to redeem a given offer.
    Data Visualization: Displays a visualization of a user’s past purchases.
    Web Interface: Simple web interface where users can input their user_id to receive recommendations and predictions.

Project Structure

bash

ibotta-offer-recommendation-engine/
├── app/
│   ├── main.py                  # FastAPI application
│   ├── models/
│   │   ├── prediction.py         # Handles offer redemption prediction logic
│   │   └── recommendation.py     # Handles personalized offer recommendations
├── data/
│   ├── orders.csv                # Dataset of user orders (raw)
│   ├── cleaned_orders.csv        # Preprocessed dataset (generated by notebook)
├── notebooks/
│   ├── data_preprocessing.ipynb  # Jupyter notebook for data preprocessing
├── templates/
│   ├── index.html                # HTML template for the frontend
├── .gitignore                    # Git ignore file
├── LICENSE                       # License information
├── README.md                     # Project README
└── requirements.txt              # Python dependencies

Setup and Installation

Follow these steps to set up and run the project on your local machine or in a cloud-based environment like GitHub Codespaces.
1. Clone the Repository

bash

git clone https://github.com/your-username/ibotta-offer-recommendation-engine.git
cd ibotta-offer-recommendation-engine

2. Set Up Virtual Environment (Optional but Recommended)

Set up a Python virtual environment to manage dependencies:

bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies

Make sure you have all the required dependencies installed. You can install them from the requirements.txt file:

bash

pip install -r requirements.txt

4. Set Up the Data

The orders.csv file must be unzipped and preprocessed to create cleaned_orders.csv. You can do this using the provided Jupyter notebook:

    Open the data_preprocessing.ipynb notebook.
    Run the notebook to preprocess the orders.csv file and generate the cleaned_orders.csv file.
    Make sure that the cleaned_orders.csv file is saved in the data/ directory.

5. Running the Application

Once everything is set up, you can run the FastAPI application using Uvicorn:

bash

uvicorn app.main:app --reload

The application will be available at http://127.0.0.1:8000.
How to Use
1. Web Interface for Offer Recommendations

    Open your browser and go to http://127.0.0.1:8000.
    You will see a simple form where you can input a user_id to get personalized recommendations.
    The page will display a list of recommended offers and a chart of the user's past purchase behavior.

2. Offer Redemption Prediction

You can use tools like Postman or curl to test the offer redemption prediction feature. Here's an example of how to send a request:

    POST request to: http://127.0.0.1:8000/predict/

Request Body:

json

{
    "user_id": 1,
    "offer_id": 203,
    "features": {
        "purchase_history": 12,
        "time_of_day": "morning"
    }
}

Example Response:

json

{
    "offer_redeemed": true
}

Example Input Data

The datasets are based on past purchases, and the following fields are expected:

    user_id: The unique ID of the user.
    offer_id: The unique ID of the offer.
    purchase_history: Number of past purchases by the user.
    time_of_day: Time of day when the offer was redeemed (morning, afternoon, evening).

Preprocessing Data

The data preprocessing notebook data_preprocessing.ipynb helps with cleaning the raw orders.csv file. You can preprocess the data by loading it and handling missing values as demonstrated in the notebook. The cleaned data is then used for recommendations and predictions.
Technologies Used

    Backend: FastAPI, Uvicorn
    Data Processing: pandas, scikit-learn
    Frontend: Jinja2 (HTML templating)
    Data Visualization: Plotly (optional)
    Deployment: GitHub Codespaces (or any local environment)

Future Improvements

    Advanced Recommendation Models: Implement collaborative filtering or a content-based filtering algorithm.
    Improved Prediction Accuracy: Train the machine learning model with real-world data and fine-tune it.
    Enhanced UI: Improve the user interface with CSS frameworks like Bootstrap.

License

This project is licensed under the MIT License - see the LICENSE file for details.