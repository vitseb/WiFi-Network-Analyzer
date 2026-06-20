class WifiNetworkData:
    def __init__(self, ssid, rssi, channel, authentication_type, encryption_type): # Constructor
        self.ssid = ssid
        self.rssi = rssi
        self.channel = channel
        self.authentication_type = authentication_type
        self.encryption_type = encryption_type  