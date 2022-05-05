
import json
import requests
url ='http://127.0.0.1:8000/drinks/'
response = requests.get(url)
print(json.dumps(response.json()))
drinks = json.loads(json.dumps(response.json()))
for drink in drinks:
    print(drink['id'])
# print(pairs.iyr)
# for key, values in pairs:
#      for key,item in values:
#          print(item)