import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
        # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

if len(sys.argv) > 2:
    output_file = sys.argv[2]
    with open(output_file, 'w') as yaml_file:
        yaml.dump(
            source_content,
            yaml_file,
            allow_unicode=True
        )
else:
    print(yaml.dump(source_content))