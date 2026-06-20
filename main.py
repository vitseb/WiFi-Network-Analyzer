from scanner.wifi_scanner import scan_wifi
from analyzers.signal_analyzer import get_quality
from analyzers.security_analyzer import analyze_security_protocol, get_warning
from exporters.json_exporter import export_to_json
from exporters.csv_exporter import export_to_csv
from history.history_manager import save_scan, load_scan

def main():
    networks = []
    
    while True:
        print("\n--- WiFi Analyzer ---")
        print("1. Scan networks")
        print("2. View history")
        print("3. Export results")
        print("4. Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            # call scan_wifi(), store result in networks, print each network
            networks = scan_wifi()
            for network in networks:
                print(f"{network.ssid} | {network.rssi} dBm ({get_quality(network.rssi)}) | {network.authentication_type} - {analyze_security_protocol(network.authentication_type)}")            
            save_scan(networks)
        elif choice == "2":
            # ask for filename, call load_scan(), print result
            filename = input("Enter filename: ")
            networks = load_scan(filename)
            for network in networks:
                print(f"{network.ssid} | {network.rssi} dBm ({get_quality(network.rssi)}) | {network.authentication_type} - {analyze_security_protocol(network.authentication_type)}")            
        elif choice == "3":
            # ask json or csv, call right exporter
            filename = input("Enter filename (json/csv): ")
            if filename.endswith('.json'):
                export_to_json(networks, filename)
            elif filename.endswith('.csv'):
                export_to_csv(networks, filename)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()