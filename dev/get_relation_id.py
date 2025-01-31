import requests
import json

# Define the place name and API endpoint
place_name = "Arizona, US"
url = f"https://nominatim.openstreetmap.org/search?q={place_name}&format=json"

# Custom headers
headers = {
    "User-Agent": "YourAppName/1.0 (your_email@example.com)"
}

try:
    # Send the request
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise exception for HTTP errors
    data = response.json()

    # Extract relation ID if available
    if data:
        osm_id = data[0].get("osm_id")
        print(f"OSM Relation ID: {osm_id}")
    else:
        print("No data found for the place.")
except Exception as e:
    print(f"An error occurred: {e}")
