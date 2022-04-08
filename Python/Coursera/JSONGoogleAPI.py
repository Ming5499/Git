import urllib.request, urllib.error, urllib.parse
import json

service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = service_url + urllib.parse.urlencode({'address':address})
    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print(('Retrieved', len(data), 'characters'))
    try:
        js = json.loads(data)
    except:
        js:None
    if not js or 'status' not in js or js['status']!= 'OK':
        print('====Failture To ReTrieve====')
        print(data)
        continue
lat = js["result"][0]["geometry"]["location"]["lat"]
lng = js["result"][0]["geometry"]["location"]["lng"]
print('lat',lat,'lng',lng)
location = js['results'][0]['formatted_address']
print(location)
