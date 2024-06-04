import json
import os
import random

def get_machine_info():
    base_name = os.getenv('MACHINE_BASE_NAME', 'OPENSHIFT_VIRT')
    machine_name = f"{base_name}_{random.randint(1, 1000)}"
    
    # Get IP address octets from environment variables
    octet1 = os.getenv('IP_OCTET1', '192')
    octet2 = os.getenv('IP_OCTET2', '168')
    octet3 = os.getenv('IP_OCTET3', '1')
    octet4 = str(random.randint(10, 200))  # Generate random octet for fourth part of the IP address
    ip_address = f"{octet1}.{octet2}.{octet3}.{octet4}"

    # Generate MAC address
    mac_address = ':'.join(['52', '54', '00'] + [format(int(255 * random.random()), '02x') for _ in range(3)])
    
    return machine_name, ip_address, mac_address

if __name__ == "__main__":
    machine_name, ip_addresses, mac_address = get_machine_info()
    print(json.dumps({"machine_name": machine_name, "ip_addresses": ip_addresses, "mac_address": mac_address}))
