import requests
import os
from dotenv import load_dotenv
from pprint import pprint

class VK:
	API_BASE_URL = 'https://api.vk.com/method'
	def __init__(self, access_token, user_id):
		self.token = access_token
		self.user_id = user_id

	def get_common_params(self):
		return {
			"access_token": self.token,
			"v": "5.131",
		}

	def _build_url(self, api_method):
		return f"{self.API_BASE_URL}/{api_method}"

	def user_info(self):
		params = self.get_common_params()
		params.update({"user_id": self.user_id})
		response = requests.get(self._build_url("users.get"), params=params)
		return response.json()

	def get_status(self):
		params = self.get_common_params()
		params.update({"user_id": self.user_id})
		response = requests.get(self._build_url("status.get"), params=params)
		return response.json().get("response", {}).get("text")

	def get_profile_photos(self):
		params = self.get_common_params()
		params.update({"user_id": self.user_id, "album_id": "profile"})
		response = requests.get(self._build_url("photos.get"), params=params)
		return response.json()


if __name__ == "__main__":
	load_dotenv()
	vk_token = os.getenv("VK_API")
	user_id = "1"
	vk = VK(vk_token, user_id)
	print(vk.user_info())
	print(vk.get_status())
	pprint(vk.get_profile_photos())

