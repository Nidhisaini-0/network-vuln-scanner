import socket
from datetime import datetime

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        s.close()
        return result == 0
    except: 
        return False

def main():
    print("=" * 50)
    print("    BASIC NETWORK VULNERABILITY SCANNER")
    print("=" * 50)

    target = input("Enter target IP (default: 127.0.0.1): ")
    if target.strip() == "":
        target = "127.0.0.1"


    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    print ("\nScanning started at:", datetime.now())
    print("-" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"[OPEN] Port {port}")
            open_ports.append(port)
    
    print("\nScan finished at:", datetime.now())

    if open_ports:
        print("\nOpen Ports Found:")
        for p in open_ports:
            print("Port", p)
    else:
        print("\nNo open ports found.")

    
    # Save results to file

    with open("scan_result.txt", "w") as f:
        f.write("Network Vulnerability Scan Report\n")
        f.write(f"Target: {target}\n")
        f.write(f"Time: {datetime.now()}\n\n")

        if open_ports:
            f.write("Open Ports:\n")
            for p in open_ports:
                f.write(f"Port {p}\n")
        else:
            f.write("No open ports found.\n")
    
    print("\nResults saved to scan_result.txt")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except ValueError:
        print("\nInvalid input! Please enter numeric port values.")
    except socket.gaierror:
        print("\nInvalid IP address or unreachable host.")
