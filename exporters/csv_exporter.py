import csv

def export_to_csv(networks, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['SSID', 'RSSI', 'Channel', 'Authentication_type', 'Encryption_type'])
        for n in networks:
            writer.writerow([n.ssid, n.rssi, n.channel, n.authentication_type, n.encryption_type])