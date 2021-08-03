import json
import sys

# Usage: python convert_json.py source event_bus_name detail_type

with open('input.json', 'r') as fp:
    sample = json.load(fp)
template = [{
                "Source": sys.argv[1], 
                "Detail": json.dumps(sample), 
                "Resources": [],
                "EventBusName": sys.argv[2],
                "DetailType": sys.argv[3]
            }]
with open('output.json','w') as fp:
    json.dump(template,fp)
            