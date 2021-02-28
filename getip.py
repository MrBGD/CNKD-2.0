import requests 
import json
request=requests.get("https://api.ipify.org?format=json")
jsoned=json.loads(request.text)
print(jsoned["ip"])