import requests
import json

def get_machine_info(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data['machine_name'], data['ip_addresses'], data['mac_address']

if __name__ == "__main__":
    api_url = "<API_URL>"  # Replace with your API URL
    machine_name, ip_addresses, mac_address = get_machine_info(api_url)
    print(json.dumps({"machine_name": machine_name, "ip_addresses": ip_addresses, "mac_address": mac_address}))