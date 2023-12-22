import socket
import subprocess
from _datetime import datetime

target = input("Enter The Target IP: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"Scanning {ip}")
        print("Time Started: ", datetime.now())

        for port in range(20,65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()
    except socket.gaierror:
        print("Hostname Could Not Be Resolved")
    except socket.error:
        print("Could not connect to the server")
port_scan(target)