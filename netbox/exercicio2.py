#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

import requests

netbox_url_api_devices = "http://localhost:8000/api/dcim/devices/"
token = "c37c796a6b2155e4caa519b3ebb077b6f261dda8"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+token
}

response_get_interfaces = requests.request("GET", netbox_url_api_devices, headers=headers, verify=False)


for device in response_get_interfaces.json()['results']:
    #print(device)
    print(f"device: {device['name']} - ip: {device['primary_ip']['address']}")


