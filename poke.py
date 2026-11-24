import json
import requests

# Remember to remove the '#' symbol
# before code statments so you can run them!

# JSON example 1:
#squirtleJSON = '{ "name": "Squirtle", "type": "water", "weight": 9.0}'
#squirtleDict = json.loads(squirtleJSON) # Parse squirtleJSON
#print(pokemonDict["weight"]) # We now have a Python Dictionary


# JSON example 2:
#pikachuDict = {
#    "name" : "Pikachu",
#    "type" : "electric",
#    "weight" : 6.0
#}
#pikachuJSON = json.dumps(pikachuDict) # Convert Python dict to JSON
#print(pikachuJSON) # We now have a JSON string

# JSON example 3: Don't worry if you don't understand the code! That will be explained as we go:
#response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
#print(json.dumps(response.json())) # LOOK HERE. Very hard to read!

# JSON example 4:
#response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
#print(json.dumps(response.json(), indent = 4)) # LOOK HERE. Very hard to read!

#-----------------------------------------------------------------------------------------------------

# API example 1:
#response = requests.get("INSERT URL HERE")
#print(response)


# API example 2:
#response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
#pikachuMoves = response.json()["moves"]
#for move in pikachuMoves:
#    print(move["move"]["name"]) # These are all Pikachu's moves! You might recognise them


# API example 3:
#response = requests.get("https://httpbin.org/status/400")
#print(response.status_code)
#response.raise_for_status()


# API example 4:
#url = "https://reqres.in/api/users" # Endpoint
#params = {"page": 2} # same as "page=2"

#response = requests.get(url, params= params)
#print("Final URL:", response.url) # shows https://reqres.in/api/users?page=2
#print(json.dumps(response.json(), indent = 4))


# API example 5:
#token = "aCKo4"
#url = "https://httpbin.org/bearer"

# We put the authorization as a key/value pair:
#header = {
#    "Authorization" : f"Bearer {token}"
#}

#response = requests.get(url, headers= header) # then put the header with the request

#print("Status code:", response.status_code)
#print("URL:", response.url)

#data = response.json()
#print(data)


# API example 6:
#url = "https://jsonplaceholder.typicode.com/posts"

# The JSON we want to send
#payload = {
#    "title": "Hello from Python",
#    "body": "This is a test post",
#    "userId": 1
#}

#response = requests.post(url, json= payload)

#print("Status code:", response.status_code) # Should be 201 for a successful POST request
#data = response.json()
#print(data)

# API example 7:
#url = "https://jsonplaceholder.typicode.com/posts/3"
#response = requests.delete(url) # Deleting post 3
#print("Status code:", response.status_code)

# API example 8:
#url = "https://jsonplaceholder.typicode.com/posts/5"

#updatedPost = {
#    "title": "Mohamed was here!",
#    "body": "I like squirtle!",
#    "userId": 1
#}
#response = requests.put(url, data= updatedPost)
#print("Status code:", response.status_code)

#updatedField = {
#    "title": "Vishnu is goated!"
#}
#secondResponse = requests.patch(url, data= updatedField)
#print("Status code:", secondResponse.status_code)
