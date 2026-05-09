import socket
from datetime import datetime

# Scan single port
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        sock.close()

    except:
        pass

# Main scanner
def main():
    target = input("Enter target IP or website: ")

    try:
        target_ip = socket.gethostbyname(target)

    except socket.gaierror:
        print("Invalid target.")
        return

    print(f"\nScanning Target: {target_ip}")
    print(f"Started at: {datetime.now()}\n")

    # Common ports
    ports = [
        20, 21, 22, 23, 25,
        53, 80, 110, 135,
        139, 143, 443, 445,
        3306, 3389
    ]

    for port in ports:
        scan_port(target_ip, port)

    print("\nScan completed.")

if __name__ == "__main__":
    main()