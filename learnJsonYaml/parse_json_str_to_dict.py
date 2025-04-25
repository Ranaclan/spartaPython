import json

with open("servers.json", "r") as json_file:
    json_str = json_file.read() #this reads the json_file and stores its contents as a string
    servers = json.loads(json_str) #the json.loads method takes in a string, so passing the string version of the file works

print(type(servers))
print(servers["server1"])
print(servers["server2"])

for key, value in servers.items():
    print(f"Key and value: '{key}' = '{value}'")

    for sub_key, sub_value in value.items():
        print(f"Record key and sub value: '{sub_key}' = '{sub_value}'")