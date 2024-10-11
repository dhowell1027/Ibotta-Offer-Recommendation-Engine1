import os
import kaggle

def download_instacart_data():
    # Specify the dataset on Kaggle
    dataset = 'instacart/instacart-market-basket-analysis'

    # Directory where the dataset will be saved
    data_dir = 'data/raw/'

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download the dataset
    kaggle.api.dataset_download_files(dataset, path=data_dir, unzip=True)
    print(f"Instacart data downloaded to {data_dir}")

if __name__ == "__main__":
    download_instacart_data()
