import os
from dotenv import load_dotenv
import pandas as pd
import requests

def extract():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()

def transform(data):
    return pd.DataFrame(data)

def load(df):
    print("Loaded data:")
    print(df.head())

def main():
    load_dotenv()
    data = extract()
    df = transform(data)
    load(df)

if __name__ == "__main__":
    main()