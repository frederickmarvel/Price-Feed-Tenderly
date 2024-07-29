import requests
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv('DUNE_API_KEY')

# Define the API endpoint and parameters
url = "https://api.dune.com/api/v1/query/2694992/results"
headers = {
    'x-dune-api-key': api_key
}
params = {
    'limit': 5000000
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Convert data to a DataFrame
    df = pd.json_normalize(data['result']['rows'])

    # Save DataFrame to CSV
    df.to_csv('dune_data.csv', index=False)
    print("Data saved to dune_data.csv")
else:
    print(f"Failed to fetch data: {response.status_code}")

