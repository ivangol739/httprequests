import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

yandex_token = os.getenv("TOKEN")
url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"


def translate_word(word):
	params = {
		"key": yandex_token,
		"lang": "ru-en",
		"text": word
	}

	response = requests.get(url, params=params)
	if response.status_code == 200:
		data = response.json()
		return data["def"][0]["tr"][0]["text"]
	else:
		return f"Ошибка: {response.status_code}"


if __name__ == "__main__":
	word = "машина"
	print(translate_word(word))