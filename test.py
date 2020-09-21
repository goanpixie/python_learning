import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")

data = response.json()
# print(data)

repository = data[0]
# print(repository)

userIds = [item.get('userId') for item in data]

print(userIds)
