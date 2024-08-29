import polyline
import base64
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
#FLAG IS AT line 236
# Initialize the geocoder
geolocator = Nominatim(user_agent="geoapiExercises")
# Rate limiter to respect Nominatim's API limits
reverse_geocode = RateLimiter(geolocator.reverse, min_delay_seconds=1)
def _decode_locations():
    #uses Nominatim, which is rate-limited
    with open("locations.txt", "r+") as f:
        for line in f.readlines():
            line = base64.b64decode(line).decode('utf-8')
            latitude, longitude = polyline.decode(line)[0]
            import time
            reverse_geocode_check(latitude, longitude)
            time.sleep(1) #due to nominatim's api limit of 1 call/s
            # location = geolocator.reverse((latitude, longitude), exactly_one=True) 
def reverse_geocode_check(lat, lon):
    location = reverse_geocode((lat, lon), exactly_one=True)
    if location:
        print(f"Location: {location.address}")
    else:
        print(f"No location found for coordinates: {lat}, {lon}")
if __name__ == "__main__":
    _decode_locations()