import requests
import json

url = "http://127.0.0.1:5000/topics/add"
data = {"user" : "srijit", "topic" : "FOP"}
headers = {'content-type': 'application/json'}
r = requests.post(url, data = json.dumps(data), headers = headers)
print(r.content)
