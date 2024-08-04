import requests
import json
from pprint import pprint


def get_the_smartest_superhero():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    the_smartest_superhero = ''
    max_intelligence = 0
    if response.status_code == 200:
        heroes = ["Hulk", "Captain America", "Thanos"]
        superheroes = response.json()
        for hero in superheroes:
            if hero["name"] in heroes:
                intelligence = hero["powerstats"]["intelligence"]
                if intelligence > max_intelligence:
                    max_intelligence = intelligence
                    the_smartest_superhero = hero["name"]
    else:
        print("API error")
    return the_smartest_superhero

print(get_the_smartest_superhero())