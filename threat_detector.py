
import random
from datetime import datetime

AUTHORIZED_USERS = {"admin": "admin123", "pilot": "pilot456"}

NETWORK_TRAFFIC = [
    {"ip": "192.168.1.1", "timestamp": "2025-03-01 10:00:00", "data_transferred": 100},
    {"ip": "192.168.1.2", "timestamp": "2025-03-01 10:01:00", "data_transferred": 5000},
    {"ip": "192.168.1.3", "timestamp": "2025-03-01 10:02:00", "data_transferred": 200},
]

def detect_unauthorized_access(username, password):
    if username in AUTHORIZED_USERS and AUTHORIZED_USERS[username] == password:
        return False
    else:
        return True

def analyze_network_traffic(traffic):
    suspicious_traffic = []
    for entry in traffic:
        if entry["data_transferred"] > 1000:
            suspicious_traffic.append(entry)
    return suspicious_traffic

def generate_alert(threat_type, details):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ALERT] {timestamp}: {threat_type} detected!")
    print(f"Details: {details}")

def main():
    print("Welcome to the Aerospace Cybersecurity Threat Detector!")
    while True:
        print("\nMenu:")
        print("1. Check Unauthorized Access")
        print("2. Analyze Network Traffic")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if detect_unauthorized_access(username, password):
                generate_alert("Unauthorized Access Attempt", f"Username: {username}")
            else:
                print("Access granted. Welcome!")
        elif choice == "2":
            suspicious_traffic = analyze_network_traffic(NETWORK_TRAFFIC)
            if suspicious_traffic:
                generate_alert("Suspicious Network Traffic", suspicious_traffic)
            else:
                print("No suspicious traffic detected.")
        elif choice == "3":
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
