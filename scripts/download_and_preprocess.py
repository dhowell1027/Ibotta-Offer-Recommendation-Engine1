import pandas as pd
import os

def download_and_preprocess():
    # Ensure the data is downloaded
    if not os.path.exists('data/raw/orders.csv'):
        raise FileNotFoundError("Instacart data not found. Please run download_instacart_data.py first.")

    # Load Instacart data
    orders = pd.read_csv('data/raw/orders.csv')
    products = pd.read_csv('data/raw/products.csv')
    order_products = pd.read_csv('data/raw/order_products__prior.csv')

    # Example preprocessing step: Merge order data with product data
    merged_data = pd.merge(order_products, products, on='product_id')
    
    # Add some additional preprocessing steps as necessary...
    
    # Save preprocessed data
    merged_data.to_csv('data/processed/instacart_preprocessed.csv', index=False)
    print("Preprocessed data saved to data/processed/")

if __name__ == "__main__":
    download_and_preprocess()
