# Network Vulnerability Scanner

A basic network vulnerability scanner built with Python that scans a target host for open TCP ports and provides basic information about detected services.

This project was developed as a cybersecurity learning project to understand network scanning, TCP connections, ports, and basic service enumeration.

## Features

* Scan a specified target IP address or hostname
* Scan a range of TCP ports
* Identify open ports
* Retrieve basic service information using socket connections
* Record scan results
* Display scan progress and results
* Simple command-line interface

## Technologies Used

* **Python 3**
* **Socket Programming**
* **TCP/IP Networking**
* **Linux / Ubuntu**
* **Bash**

## Project Structure

```text
network-vuln-scanner/
│
├── scanner.py          # Main Python scanner
├── scanner.sh          # Shell script for running the scanner
├── scan.txt            # Scan input/data
├── scan_result.txt     # Example scan results
└── README.md           # Project documentation
```

## How It Works

The scanner uses Python's `socket` module to attempt TCP connections to ports on the target system.

For each port in the specified range:

1. The scanner creates a TCP socket.
2. It attempts to connect to the target port.
3. If the connection succeeds, the port is considered open.
4. Basic information about the open port can then be collected.
5. The results are recorded for later reference.

This provides a basic understanding of how network port scanning works.

## Requirements

* Python 3.x
* Linux/Ubuntu or another operating system with Python installed

No external Python libraries are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/Nidhisaini-0/network-vuln-scanner.git
```

Move into the project directory:

```bash
cd network-vuln-scanner
```

## Usage

Run the Python scanner:

```bash
python3 scanner.py
```

Follow the prompts provided by the program to enter the target and port range.

You can also use the shell script:

```bash
chmod +x scanner.sh
./scanner.sh
```

## Example

A scan may produce results similar to:

```text
Starting scan...

Target: 127.0.0.1

Scanning ports...

Port 22: OPEN
Port 80: OPEN
Port 443: OPEN

Scan completed.
```

The exact results depend on the target system and the services running on it.

## Learning Objectives

This project was created to practice:

* Python socket programming
* TCP connections
* Network ports and services
* Basic network reconnaissance
* Port scanning concepts
* Command-line security tools and scripting
* Recording and analyzing scan results

## Limitations

This is a basic educational scanner and is not intended to replace professional vulnerability scanners such as Nmap or commercial security assessment tools.

The project primarily focuses on TCP port scanning and basic service information rather than comprehensive vulnerability detection.

## Legal and Ethical Use

Use this scanner only against systems that you own or have explicit permission to test.

Unauthorized scanning of systems or networks may violate organizational policies or applicable laws.

## Future Improvements

Possible improvements include:

* Service/version detection
* Banner grabbing
* Multithreaded scanning
* Configurable scan timeouts
* Better result formatting
* Vulnerability/CVE mapping
* Exporting results to structured formats such as JSON or CSV

## Author

**Nidhi Saini**

GitHub: [Nidhisaini-0](https://github.com/Nidhisaini-0)

## License

This project is intended for educational and cybersecurity learning purposes.
