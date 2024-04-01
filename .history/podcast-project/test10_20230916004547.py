import requests
import xmltodict
from pymongo import MongoClient

# Replace with your MongoDB connection details
host = "localhost"  # Usually "localhost" for a local MongoDB server
port = 27017  # Default MongoDB port number

# Create a MongoClient instance to connect to MongoDB
client = MongoClient(host, port)
#Access a Database
db = client["podcast"]
#Access a Collection
collection = db["podcast"]


PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
data = requests.get(PODCAST_URL)
feed = xmltodict.parse(data.text)

podcast =[]
for i in range(50):
    podcast.append(feed['rss']['channel']['item'][i])

for data in podcast:
    collection.insert_one(data)
