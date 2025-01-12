import os
import urllib.request
import pandas as pd

DOWNLOAD_ROOT = "https://github.com/ageron/data/raw/main/housing/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "housing.csv"

def fetch_house_data(house_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    csv_path = os.path.join(housing_path, "housing.csv")
    urllib.request.urlretrieve(house_url, csv_path)

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

fetch_house_data()
housing = load_housing_data()
print(housing.head())
print(housing["ocean_proximity"].value_counts())