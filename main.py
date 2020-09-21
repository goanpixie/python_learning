from mymodule import test
import json
from

test()

# f = open('fake_fruits.json', 'r')
# print(f.read())
# f.close()

#with statement -

with open('fake_fruits.json', 'r') as f:   # open the JSON file for reading
  data = json.load(f)  # de-serialise the JSON into data
print(data)

data['Fruit'][1]['Name'] = 'wrong'

with open('fake_fruits.json', 'w') as f:
  json.dump(data, f, indent=4, sort_keys=True)

with open('fake_fruits.json', 'r') as f:
  print(f.read())

def addStrawberry():
  with open('fake_fruits.json', 'r') as f:
    data = json.load(f)
    strawberry = {
           "Name": "Strawberry",
           "Colour": "Red"
    }
    data['Fruit'].append(strawberry)
  return data

with open('fake_fruits.json', 'w') as f:
  json.dump(data, f, indent=4)

with open('fake_fruits.json', 'r') as f:
   print(f.read())



