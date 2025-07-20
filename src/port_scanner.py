import socket

target = input("Enter target IP address: ")
ports = [21, 22, 23, 25, 53, 80, 139, 443, 445, 8080]

print(f"Scanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()
