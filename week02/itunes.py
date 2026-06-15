import json
import sys
import requests


if len(sys.argv) !=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

storeData = response.json()

for index, result in enumerate(storeData["results"]):
    print(f"Song Name {index}: {result["trackName"]}")
# print(json.dumps(response.json(), indent= 2))