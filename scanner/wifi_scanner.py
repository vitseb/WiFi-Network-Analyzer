import sys
import model.wifi_model as WifiNetworkModel

SECURITY_MAP = {
    0:  ("Open",   "None"),
    1:  ("WEP",    "WEP"),
    2:  ("WPA",    "TKIP"),
    3:  ("WPA",    "TKIP/AES"),
    4:  ("WPA2",   "AES"),
    5:  ("WPA2",   "AES"),
    6:  ("WEP",    "Dynamic"),
    7:  ("WPA",    "TKIP"),
    8:  ("WPA",    "TKIP/AES"),
    9:  ("WPA2",   "AES"),
    10: ("WPA2",   "AES"),
    11: ("WPA3",   "SAE"),
    12: ("WPA3",   "SAE"),
    13: ("WPA3",   "SAE/AES"),
    14: ("Open",   "OWE"),
    15: ("Open",   "OWE"),
}

def scan_wifi():
    if sys.platform == "darwin":
        return _scan_macos()
    elif sys.platform == "win32":
        return _scan_windows()
    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

def _scan_macos():
    try:
        import CoreWLAN
    except ImportError:
        raise ImportError("Run: pip3 install pyobjc-framework-CoreWLAN")

    client = CoreWLAN.CWWiFiClient.sharedWiFiClient()
    iface = client.interface()
    if iface is None:
        raise RuntimeError("No WiFi interface found")

    networks, err = iface.scanForNetworksWithName_includeHidden_error_(None, True, None)
    if err:
        raise RuntimeError(f"Scan failed: {err}")

    if not networks:
        return []

    result = []
    for n in networks:
        ssid = n.ssid() or f"<hidden:{n.bssid() or 'unknown'}>"
        rssi = n.rssiValue()
        channel = n.wlanChannel().channelNumber() if n.wlanChannel() else 0
        sec_code = n.strongestSupportedSecurity()
        auth, enc = SECURITY_MAP.get(sec_code, ("Unknown", "Unknown"))
        result.append(WifiNetworkModel.WifiNetworkData(ssid, rssi, channel, auth, enc))

    return result

def _scan_windows():
    import subprocess
    result = subprocess.run(
        ['netsh', 'wlan', 'show', 'networks', 'mode=BSSID'],
        capture_output=True, text=True
    )
    networks = []
    ssid = signal = channel = auth = encryption = None

    for line in result.stdout.splitlines():
        if "SSID" in line and "BSSID" not in line:
            ssid = line.split(":")[1].strip()
        elif "Signal" in line:
            signal = int(line.split(":")[1].strip().replace("%", ""))
        elif "Channel" in line:
            channel = int(line.split(":")[1].strip())
        elif "Authentication" in line:
            auth = line.split(":")[1].strip()
        elif "Encryption" in line:
            encryption = line.split(":")[1].strip()
            networks.append(WifiNetworkModel.WifiNetworkData(ssid, signal, channel, auth, encryption))

    return networks
