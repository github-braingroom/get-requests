import requests
import json

url="https://jsonplaceholder.typicode.com/posts/1"

try:
  print("Trying to connect")
  r=requests.get(url)
  print("Successful")
except Exception as e:
  print("Failed")
  print(e)
  
txt=r.content.decode('utf-8')
data=json.loads(txt)

print(json.dumps(data,indent=4))

print(data['title'])
