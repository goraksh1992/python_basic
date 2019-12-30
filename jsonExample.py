import json

json_string = '{"name" : "gaurav sanas", "age" : 27}'

x = json.loads(json_string)

print(x)

# NOTE : json.loads(json_string) function used to convert json string to json