import requests
import os
from dotenv import load_dotenv


class VK:
	def __init__(self, access_token, user_id, version="5.131"):
		self.token = access_token
		self.user_id = user_id
		self.version = version
		self.params = {
			"access_token": self.token,
			"v": self.version,
		}

	def user_info(self):
		url = 'https://api.vk.com/method/users.get'
		params = {"user_id": self.user_id}
		response = requests.get(url, params={**self.params, **params})
		return response.json()


if __name__ == "__main__":
	load_dotenv()
	vk_token = os.getenv("VK_API")
	user_id = "1"
	vk = VK(vk_token, user_id)
	print(vk.user_info())
