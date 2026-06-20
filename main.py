import os
from scanner.wifi_scanner import scan_wifi
from analyzers.signal_analyzer import get_quality
from analyzers.security_analyzer import analyze_security_protocol, get_warning
from exporters.json_exporter import export_to_json
from exporters.csv_exporter import export_to_csv
from history.history_manager import save_scan, load_scan, list_scans

def print_networks(networks):
    if not networks:
        print("  No networks found.")
        return
    header = f"{'SSID':<32} {'Signal':>9}  {'Quality':<10} {'Ch':>3}  {'Auth':<8} {'Rating'}"
    print()
    print(header)
    print("-" * len(header))
    for n in networks:
        quality = get_quality(n.rssi)
        rating = analyze_security_protocol(n.authentication_type)
        print(f"{n.ssid:<32} {n.rssi:>6} dBm  {quality:<10} {n.channel:>3}  {n.authentication_type:<8} {rating}")

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
            networks = scan_wifi()
            print_networks(networks)
            save_scan(networks)
        elif choice == "2":
            files = list_scans()
            if not files:
                print("  No saved scans found.")
            else:
                for i, f in enumerate(files, 1):
                    print(f"  {i}. {os.path.basename(f)}")
                pick = input("Choose: ")
                if pick.isdigit() and 1 <= int(pick) <= len(files):
                    networks = load_scan(files[int(pick) - 1])
                    print_networks(networks)
                else:
                    print("  Invalid choice.")
        elif choice == "3":
            if not networks:
                print("  No networks to export. Run a scan first.")
            else:
                filename = input("Enter filename (.json or .csv): ")
                if filename.endswith('.json'):
                    export_to_json(networks, filename)
                    print(f"  Exported to {filename}")
                elif filename.endswith('.csv'):
                    export_to_csv(networks, filename)
                    print(f"  Exported to {filename}")
                else:
                    print("  Error: filename must end in .json or .csv")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()