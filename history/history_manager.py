import json
import os
import datetime
from model.wifi_model import WifiNetworkData

def save_scan(networks):
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"data/scan_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump([n.__dict__ for n in networks], f, indent=2)

def list_scans():
    if not os.path.exists("data"):
        return []
    files = sorted([f for f in os.listdir("data") if f.endswith(".json")], reverse=True)
    return [os.path.join("data", f) for f in files]

def load_scan(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return [WifiNetworkData(**item) for item in data]