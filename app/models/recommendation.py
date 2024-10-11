import pandas as pd

# Example dataset of offers
offers = pd.DataFrame({
    'offer_id': [1, 2, 3, 4],
    'product': ['Milk', 'Eggs', 'Bread', 'Cheese'],
    'category': ['Dairy', 'Dairy', 'Bakery', 'Dairy']
})

# Function to get recommendations for a user
def get_recommendations(user_id: int):
    # Placeholder: Mock recommendation logic
    # In real-world use, this would be based on user's purchase history and advanced recommendation logic
    recommended_offers = offers.sample(n=2)  # Randomly recommending 2 offers
    return recommended_offers.to_dict(orient='records')
