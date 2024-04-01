# pip install geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test")
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)
#Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
print((location.latitude, location.longitude))
#(52.5094982, 13.3765983)
