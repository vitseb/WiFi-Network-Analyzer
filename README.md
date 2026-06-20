# WiFi Network Analyzer

## Overview

WiFi Network Analyzer is a Python application that scans nearby wireless networks, analyzes their security and signal quality, and allows users to export scan results for further analysis.

## Features

### Network Scanning

Display information such as:

* SSID
* Signal Strength (RSSI)
* Channel
* Authentication Type
* Encryption Type

### Signal Analysis

Convert signal values into categories:

| RSSI       | Quality   |
| ---------- | --------- |
| -30 to -70 | Excellent |
| -71 to -80 | Good      |
| -81 to -90 | Fair      |
| -91+       | Weak      |

### Security Analysis

Evaluate detected networks:

* Open Network
* WEP
* WPA
* WPA2
* WPA3

Generate warnings and recommendations when weak security is detected.

### Data Export

Support exporting scan results to:

* JSON
* CSV

### Scan History

Store previous scans locally and allow them to be reviewed later.

### Statistics

Generate statistics such as:

* Total networks found
* Number of WPA3 networks
* Number of open networks
* Strongest network
* Average signal strength

---

## Project Structure

```text
wifi-analyzer/
│
├── main.py
│
├── models/
│   └── wifi_network.py
│
├── scanner/
│   └── wifi_scanner.py
│
├── analyzers/
│   ├── signal_analyzer.py
│   └── security_analyzer.py
│
├── exporters/
│   ├── csv_exporter.py
│   └── json_exporter.py
│
├── history/
│   └── history_manager.py
│
├── data/
│
└── README.md
```

---

## Core Classes

### WifiNetwork

Represents a single wireless network.

Responsibilities:

* Store network information.
* Provide a structured data model.

### WifiScanner

Responsible for:

* Executing system commands.
* Parsing command output.
* Creating WifiNetwork objects.

### SignalAnalyzer

Responsible for:

* Signal quality evaluation.
* Signal-related calculations.

### SecurityAnalyzer

Responsible for:

* Security assessment.
* Warning generation.
* Security scoring.

### ExportManager

Responsible for:

* JSON export.
* CSV export.

### HistoryManager

Responsible for:

* Saving scan history.
* Loading historical scans.

---

## Future Improvements

* PyQt6 graphical interface
* Signal strength charts
* Automatic rescanning
* Network comparison
* Rogue access point detection
* Dark mode
* PDF reports

---
