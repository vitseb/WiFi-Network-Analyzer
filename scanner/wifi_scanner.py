import subprocess
import model.wifi_model as WifiNetworkModel

def scan_wifi():
    result = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=BSSID'], capture_output=True, text=True)
    networks = []
    ssid = signal = channel = auth = encryption = None
    
    for line in result.stdout.splitlines():
        if "SSID" in line and "BSSID" not in line:
            ssid = line.split(":")[1].strip()
        elif "Signal" in line:
            # signal comes as "78%" — convert to int, remove %
            signal = int(line.split(":")[1].strip().replace("%", ""))
        elif "Channel" in line:
            # your turn — extract channel number
            channel = int(line.split(":")[1].strip())
        elif "Authentication" in line:
            # your turn — extract auth type
            auth = line.split(":")[1].strip()
        elif "Encryption" in line:
            encryption = line.split(":")[1].strip()
            networks.append(WifiNetworkModel.WifiNetworkData(ssid, signal, channel, auth, encryption))
    
    return networks
