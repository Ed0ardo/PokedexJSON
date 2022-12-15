import requests
from bs4 import BeautifulSoup
import json

URL = "https://pokemondb.net/pokedex/all"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

tbody = soup.find("tbody")
trs = tbody.find_all("tr")
pokedex = {}
for tr in trs:
    tds = tr.find_all("td")
    pid = tds[0].text
    if pid not in pokedex:
        pokedex[pid] = {"name": tds[1].find("a").text, "photo":"https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + pid + ".png", "desc":"https://www.pokemon.com/us/pokedex/" + pid, "types": list(filter(None, tds[2].text.split(" ")))}

with open("newPokedex.json", "w") as f:
    json.dump(pokedex, f, indent=4)