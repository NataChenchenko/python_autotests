import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '77f3c6336fafef2849023a00994b9622'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "69859",
    "name": "eleven",
    "photo_id": 2
}

body_addpokeball = {
    "pokemon_id": "69859"
}



responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)

message = responce_create.json()['message']



responce_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(responce_change.text)


responce_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
print(responce_addpokeball.text)