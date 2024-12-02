import psutil
import time

# Function to monitor CPU and memory usage
def monitor_resources():
    print("Monitoring CPU and memory usage on the victim machine...")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=0)  # Non-blocking CPU usage
            memory = psutil.virtual_memory().percent  # Measure memory usage
            print(f"Victim Machine - CPU Usage: {cpu}% | Memory Usage: {memory}%", flush=True)
            time.sleep(1)  # Log resource usage every second
    except KeyboardInterrupt:
        print("Monitoring stopped.")

# Start monitoring
if __name__ == "__main__":
    monitor_resources()
