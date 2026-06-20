import json

def export_to_json(networks, filename):
    with open(filename, 'w') as f:
        json.dump([n.__dict__ for n in networks], f, indent=2)