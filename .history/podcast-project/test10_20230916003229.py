import requests
import xmltodict
PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
data = requests.get(PODCAST_URL)
feed = xmltodict.parse(data.text)

podcast =[]
for i in range(4):
    podcast.append(feed['rss']['channel']['item'][i])
print(podcast)
