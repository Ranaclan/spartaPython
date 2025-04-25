import requests
import json

postcodes_get_request = requests.get("https://api.postcodes.io/postcodes/E81JB")
postcodes_dict = postcodes_get_request.json()
print(postcodes_dict)

bulk_postcodes = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
bulk_headers = {"Content-Type": "application/json"}
postcodes_post_request = requests.post("https://api.postcodes.io/postcodes/", headers=bulk_headers, data=bulk_postcodes)
print(json.dumps(postcodes_post_request.json(), indent=4))