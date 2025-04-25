import os
import sys
import yaml

if len(sys.argv) > 1:
    #check folder
    path = Path(directory)
    if not path.is_dir():
        print(f"Error: {directory} is not a valid directory", file=sys.stderr)

else:
    print("ERROR: No YAML folder was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML folder>")