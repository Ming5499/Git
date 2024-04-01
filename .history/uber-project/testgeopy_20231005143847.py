# pip install geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test")
location = geolocator.reverse("40.765152, -73.976746")
location2 = geolocator.reverse("40.695053	, -74.177170")
location3 = geolocator.reverse("40.718296	, -74.014488	")
print(location.address)

print(location2.address)
print(location3.address)

print
# print((location.latitude, location.longitude))

# print(location.raw)