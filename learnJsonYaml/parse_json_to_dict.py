import json

with open("servers.json", "r") as json_file:
    servers = json.load(json_file)

print(type(servers))
print(servers["server1"])
print(servers["server2"])

for key, value in servers.items():
    print(f"Key and value: '{key}' = '{value}'")

    for sub_key, sub_value in value.items():
        print(f"Record key and sub value: '{sub_key}' = '{sub_value}'")