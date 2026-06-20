import json
import datetime

def save_scan(networks):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"data/scan_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump([n.__dict__ for n in networks], f)

def load_scan(filename):
    with open(filename, 'r') as f:
        return json.load(f)