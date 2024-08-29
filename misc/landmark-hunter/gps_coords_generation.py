import random
import polyline
import base64

def generate_random_coordinates(base_lat, base_lng, delta=1):
    # Generate random deltas within the range of -delta to +delta
    random_lat = base_lat + random.uniform(-delta, delta)
    random_lng = base_lng + random.uniform(-delta, delta)
    
    return random_lat, random_lng

def save_locations():
    # Generate nonsensical gps coordinates in the ocean
    base_latitude = -14.980884935154263
    base_longitude = 73.33453399721283

    # Generate a random coordinate around the base lat/lng
    with open("locations.txt", "a+") as f:
        for i in range(150):
            random_latitude, random_longitude = generate_random_coordinates(base_latitude, base_longitude)
    # Encode the polyline
            encoded_polyline = polyline.encode([(random_latitude, random_longitude)])
            # Base64 encode the polyline
            base64_encoded_polyline = base64.b64encode(encoded_polyline.encode("utf-8")).decode("utf-8")
            f.write(base64_encoded_polyline + "\n")


    with open("locations.txt", "a+") as f:
        for i in range(150):
            base_latitude = 39.996349722847434
            base_longitude = -39.25233575883648
            random_latitude, random_longitude = generate_random_coordinates(base_latitude, base_longitude)
            # Encode the polyline
            encoded_polyline = polyline.encode([(random_latitude, random_longitude)])
            # Base64 encode the polyline
            base64_encoded_polyline = base64.b64encode(encoded_polyline.encode("utf-8")).decode("utf-8")
            f.write(base64_encoded_polyline + "\n")
            # print(base64.b64encode(polyline.encode([(41.897598, 12.498408)]).encode("utf-8")).decode("utf-8")) saves the address of Machu picchu in this format as well

if __name__ == "__main__":
    save_locations()

