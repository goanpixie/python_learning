import json

#In python , JSON exists as string
p = '{"name": "Bob", "languages": ["Python", "Java"]}'

#import json module
#To work with JSON(str, file containimng JSON object), use Python's json module

#Parse json in python

#-1:JSON string parsing using json.loads() method-->return dictionary

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['name'])

#-2:File containing json object parsing using json.load() method-->return dictionary

with open('fake_fruit.json', 'r') as f:
  data = json.load(f)
print("data", data)

#converta dict to json:

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}

person_json = json.dumps(person_dict)
print(person_json)

#write JSON to a file in python

import json

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump('person_dict', json_file)
