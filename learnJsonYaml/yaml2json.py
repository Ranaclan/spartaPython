import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
        # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No YAML file was specified")
    print("Usage: yaml2json.py <source_file.yaml> <target_file.json>")

if len(sys.argv) > 2:
    output_file = sys.argv[2]
    print(type(source_content))
    with open(output_file, 'w') as json_file:
        json_file.write(json.dumps(source_content))
else:
    print(json.dumps(source_content))