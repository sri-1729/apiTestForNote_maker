import requests as re
import json

url = "http://127.0.0.1:5000/srijith/topic/stopics/add"
data = {"topic" : "fop", "stopic" : "Introduction", "description" : "Foundation of Programming", "resource" : "https://michiganvirtual.org/course/foundations-of-programming-b/#:~:text=Foundations%20of%20Programming%20(FoP)%20will,computer%20programming%20and%20software%20development."}
headers = {"content-type": 'application/json'}

r = re.post(url, data = json.dumps(data), headers = headers)
print(r.content)

