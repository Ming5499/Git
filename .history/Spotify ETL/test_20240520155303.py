# Import libraries
import pymongo
from pymongo import MongoClient
import logging as logger  # Assuming you're using this for logging
import pandas as pd  # Assuming you're using this for data manipulation
import requests
import json
import datetime


TOKEN = "BQAQXypBtnjQdnVV9_dBv_gOfh4hckYPK1OqPeY0Z2stOEESR_XwxVhJNWMPmYq5pjFRwwESd5KvLIMFGb3nXP3a2EDyyzH82btPtDSsX3scZcIZlEM"
# Client connection (assuming MongoDB is running locally on port 27017)
client = MongoClient('mongodb://localhost:27017')

# Using the database named 'spotify'
db = client.spotify

if __name__ == "__main__":

    # Define headers with Authorization including the access token
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    # Get today's date and calculate yesterday's date (modify as needed)
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)  # Changed to get data from yesterday

    # Convert yesterday to Unix timestamp in milliseconds
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    # Request data using the required endpoint and headers
    r = requests.get(
        "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(
            time=yesterday_unix_timestamp), headers=headers)

    # Process the response
    data = r.json()
    
    print(data)