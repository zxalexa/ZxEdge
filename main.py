```python id="x9k3p2"
import socket
from concurrent.futures import ThreadPoolExecutor

print("=== EdgeOne Advanced Scanner ===")

target = input("Masukkan target (domain/IP): ")

try:
    ip = socket.gethostbyname(target)
    print(f"Target IP: {ip}")
except:
    print("Target tidak valid")
    exit()

ports = [21, 22, 25, 53, 80, 110, 139, 143, 443, 445, 8080]

print("Scanning dimulai...\n")

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((ip, port))
    
    if result == 0:
        print(f"[OPEN] Port {port}")
    
    s.close()

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scan_port, ports)

print("\nScan selesai.")
