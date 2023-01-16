import json

data = '''{
    "name" : "Valentina",
    "phone" : {
        "type" : "intl",
        "number" : "1084450034"
    },
    "email" :{
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print("Name:", info["name"])
print("Email:", info["email"]["hide"])