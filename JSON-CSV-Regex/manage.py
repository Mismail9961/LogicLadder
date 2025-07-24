import json
import re


data = {"name":"Ismail Arshad","age":18}
json_string = json.dumps(data)
print(json_string)

python_data = json.loads(json_string)
print(python_data)

with open("data.json","w") as f:
    json.dump(data,f)


with open("data.json","r") as f:
    newData = json.load(f)
    print(newData)


with open("contacts.txt", "r") as file:
    content = file.read()

emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)
phones = re.findall(r'\b\d{11}\b', content)


import json

contacts = {"emails": emails, "phones": phones}

with open("extracted_contacts.json", "w") as f:
    json.dump(contacts, f, indent=4)
