import json

x = {

    "name" : "gaurav sanas",
    "age" : 27,
    "address" : "pune",
    "hobbies" : [
        {
            "hobby" : "singing",
        },
        {
            "hobby" : "dancing"
        }
    ]
}

print(json.dumps(x, indent=4))
print(json.dumps(x, separators=(".","=")))