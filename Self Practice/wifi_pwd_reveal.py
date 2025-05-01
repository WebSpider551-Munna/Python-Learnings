import subprocess
import re

def list_detected_wifi():
    try:
        # Run command to show available WiFi networks
        command = "netsh wlan show networks mode=bssid"
        output = subprocess.check_output(command, shell=True, text=True)
        
        # Parse the output
        networks = []
        current_network = {}
        
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("SSID"):
                if current_network:
                    networks.append(current_network)
                current_network = {"SSID": re.search(r"SSID \d+ : (.+)", line).group(1) if re.search(r"SSID \d+ : (.+)", line) else "Unknown"}
            elif line.startswith("Network type"):
                current_network["Type"] = re.search(r": (.+)", line).group(1)
            elif line.startswith("Authentication"):
                current_network["Authentication"] = re.search(r": (.+)", line).group(1)
            elif line.startswith("Encryption"):
                current_network["Encryption"] = re.search(r": (.+)", line).group(1)
            elif line.startswith("Signal"):
                current_network["Signal"] = re.search(r": (.+)", line).group(1)
        
        # Append the last network
        if current_network:
            networks.append(current_network)
        
        # Display detected networks
        if not networks:
            print("No WiFi networks detected.")
            return
        
        print("Detected WiFi Networks:")
        print("-" * 50)
        for network in networks:
            print(f"SSID: {network.get('SSID', 'N/A')}")
            print(f"Network Type: {network.get('Type', 'N/A')}")
            print(f"Authentication: {network.get('Authentication', 'N/A')}")
            print(f"Encryption: {network.get('Encryption', 'N/A')}")
            print(f"Signal Strength: {network.get('Signal', 'N/A')}")
            print("-" * 50)
            
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve WiFi networks. Ensure WiFi is enabled and try running as Administrator.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    print("Scanning for WiFi networks...\n")
    list_detected_wifi()