import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

maps_token = os.getenv("MAPS_TOKEN")


def find_uk_city(coordinates):
	british_cities = {'Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York'}
	for latitude, longitude in coordinates:
		url = f"https://geocode.maps.co/reverse?lat={latitude}&lon={longitude}&api_key={maps_token}"
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			if "address" in data:
				city = data["address"].get("city")
				if city in british_cities:
					return city

if __name__ == '__main__':
	_coordinates = [
  	('55.7514952', '37.618153095505875'),
    ('52.3727598', '4.8936041'),
    ('53.4071991', '-2.99168')
  ]
	print(find_uk_city(_coordinates))