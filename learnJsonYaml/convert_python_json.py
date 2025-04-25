# create the dictionary
import json

servers_dict = {
    "server1": {
            "hostname": "web-server-1",
            "ip_address": "192.168.1.1",
            "role": "web",
            "status": "active"
        },
    "server2": {
            "hostname": "db-server-1",
            "ip_address": "192.168.1.2",
            "role": "database",
            "status": "maintenance"
        }
}
print(json.dumps(servers_dict, indent=4))