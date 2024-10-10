import subprocess
import os
import pandas as pd

DATA_DIR = "data"
COMPETITION_NAME = "instacart-market-basket-analysis"

def download_data():
    """Download dataset from Kaggle if not already downloaded."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    # Check if the dataset has already been downloaded
    if not os.path.exists(f'{DATA_DIR}/orders.csv'):
        kaggle_download_command = f'kaggle competitions download -c {COMPETITION_NAME} -p {DATA_DIR}'
        unzip_command = f'unzip {DATA_DIR}/{COMPETITION_NAME}.zip -d {DATA_DIR}'
        
        print("Downloading dataset from Kaggle...")
        subprocess.run(kaggle_download_command, shell=True)
        
        print("Unzipping the dataset...")
        subprocess.run(unzip_command, shell=True)
        
        print("Dataset downloaded and unzipped successfully.")
    else:
        print("Dataset already exists. Skipping download.")

def preprocess_data():
    """Preprocess the data and save cleaned version."""
    print("Loading raw orders data...")
    orders = pd.read_csv(f'{DATA_DIR}/orders.csv')

    # Sample preprocessing steps
    orders.fillna(0, inplace=True)
    orders['total_orders'] = orders.groupby('user_id')['order_id'].transform('count')
    orders['time_of_day'] = orders['order_hour_of_day'].apply(lambda x: 'morning' if 5 <= x < 12 else 'afternoon' if 12 <= x < 17 else 'evening' if 17 <= x < 21 else 'night')

    print("Saving cleaned data to 'cleaned_orders.csv'...")
    orders.to_csv(f'{DATA_DIR}/cleaned_orders.csv', index=False)
    print("Preprocessing completed.")

if __name__ == "__main__":
    download_data()
    preprocess_data()
