#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

import requests, os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

netbox_url_api_devices = "http://localhost:8000/api/dcim/devices/"
token = "c37c796a6b2155e4caa519b3ebb077b6f261dda8"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+token
}

response_get_interfaces = requests.request("GET", netbox_url_api_devices, headers=headers, verify=False)


for device in response_get_interfaces.json()['results']:
    ip_mgmt = device['primary_ip']['address']
    ip_mgmt = ip_mgmt.split("/")
    ip_mgmt = ip_mgmt[0]
    
    router = {"device_type": "cisco_xr","host": ip_mgmt,"username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}
    
    try:
        print(f"Acessando device: {device['name']}")
        r1_connection = ConnectHandler(**router)

        results = r1_connection.send_command('show ip int brief', use_textfsm=True)
        
        for interface in results:
            print(interface)

        r1_connection.disconnect()
        print(f"Finalizando o acesso no device: {device['name']}")
    except Exception as err:
        print(err)


