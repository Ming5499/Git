# Import libraries
import pymongo
from pymongo import MongoClient
import logging as logger  # Assuming you're using this for logging
import pandas as pd  # Assuming you're using this for data manipulation
import requests
import json
import datetime


TOKEN = "BQAQXypBtnjQdnVV9_dBv_gOfh4hckYPK1OqPeY0Z2stOEESR_XwxVhJNWMPmYq5pjFRwwESd5KvLIMFGb3nXP3a2EDyyzH82btPtDSsX3scZcIZlEM"


def validate(df):
    """
    Validate the data
    """

    # is data empty?
    if df.empty:
        print("No songs downloaded. Finishing execution.")
        return False
    
    # primary key constraint
    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise Exception("Primary key constraint is violated!")

    # check for nulls
    if df.isnull().values.any():
        raise Exception("Missing values exist!")

if __name__ == "__main__":
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token = TOKEN)
    }

    # I want to see what I have played in the last 365 days
    today = datetime.datetime.now()
    last_year = today - datetime.timedelta(days=365)
    last_year_unix = int(last_year.timestamp()) * 1000

    # get data
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=last_year_unix),
        headers = headers)
    data = r.json()

    # diagnose
    print(data)