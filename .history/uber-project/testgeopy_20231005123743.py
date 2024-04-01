# pip install geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test")
location = geolocator.reverse("-73.976746, 40.765152")
print(location.address)
print((location.latitude, location.longitude))

