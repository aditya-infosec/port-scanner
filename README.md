# port-scanner
A basic Python port scanner built as a beginner cybersecurity project



# 🔍 Simple Python Port Scanner

This is a basic TCP port scanner written in Python using the `socket` module. It allows you to check if common ports are open on a given IP address. It's a beginner-friendly tool made for learning purposes, ethical hacking practice, or quick internal scans on your own network.

---

## 🚀 How It Works

You provide an IP address (like `127.0.0.1`), and the script tries to connect to a list of commonly used ports — such as: 21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS),
80 (HTTP), 139 (NetBIOS), 443 (HTTPS), 445 (SMB), 8080 (Alt HTTP)

If a connection is successful, the script will report that the port is **OPEN**.

---

## 🛠️ Setup

### Requirements
This script uses only built-in Python libraries, so no external packages are needed.

### Run the Scanner

1. Clone or download this repo.
2. Navigate into the project folder.
3. Run the scanner:

python src/port_scanner.py

*EXAMPLE OUTPUT*:

Enter target IP address: 127.0.0.1
Scanning 127.0.0.1...

Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN


