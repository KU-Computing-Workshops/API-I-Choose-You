import json
import requests

# Remember to remove the '#' symbol
# before code statments so you can run them!

# JSON example 1:
#squirtleJSON = '{ "name": "Squirtle", "type": "water", "weight": 9.0}'
#squirtleDict = json.loads(pokemonJSON) # Parse pokemonJSON
#print(pokemonDict["weight"]) # We now have a Python Dictionary


# JSON example 2:
#pikachuDict = {
#    "name" : "Pikachu",
#    "type" : "electric",
#    "weight" : 6.0
#}
#pikachuJSON = json.dumps(pikachuDict) # Convert Python dict to JSON
#print(pikachuJSON) # We now have a JSON string


# JSON example 4; Don't worry if you don't understand the code! That will be explained as we go:
#response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
#print(json.dumps(response.json())) # Very hard to read!

#-----------------------------------------------------------------------------------------------------

# We can also do something like this:
#pikachuMoves = response.json()["moves"]
#for move in pikachuMoves:
#    print(move["move"]["name"]) # These are all Pikachu's moves! You might recognise them

