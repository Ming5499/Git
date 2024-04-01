
import requests
import xmltodict


PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
data = requests.get(PODCAST_URL)
feed = xmltodict.parse(data.text)

print(feed)