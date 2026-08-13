# Home Network Sentinel

A Python-based network scanning tool that detects devices on a local network, identifies manufacturers by MAC address, and alerts on unknown intruders.

## Features

- ARP network scanning to discover active devices
- MAC address manufacturer identification using local IEEE OUI database
- Whitelist-based intrusion detection
- Real-time alerts for unknown devices

## Requirements

- Linux (Kali Linux recommended)
- Python 3
- Scapy library (`pip install scapy`)
- Root privileges (`sudo`)
- IEEE OUI database file (`oui.txt`) — download from https://standards-oui.ieee.org/oui/oui.txt

## Usage

1. Download the OUI database:
```bash
wget https://standards-oui.ieee.org/oui/oui.txt -O oui.txt
```

2. Add known devices to `white_list.json`:
```json
{
    "00:0c:29:ab:cd:ef": "My PC",
    "00:50:56:ff:05:c3": "Kali_VM"
}
```

3. Run the scanner:
```bash
sudo python3 arp_scan.py
```

## Author

Raymundo M. — Cybersecurity student passionate about network security and Python automation.

[GitHub Profile](https://github.com/tu_usuario)
