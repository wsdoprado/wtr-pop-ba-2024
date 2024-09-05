#!/opt/wtr/venv/bin/python3.10

import requests, os, json
from dotenv import load_dotenv
from netmiko import ConnectHandler
from napalm import get_network_driver
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
    
    router = {"hostname": ip_mgmt,"username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}
    driver = get_network_driver('iosxr')
    try:
        r_connection = driver(**router)
        r_connection.open()
        output = r_connection.get_facts() 
        print(f"device name: {output['hostname']}")
        print(f"device netbox: {device['name']}")
        
        if str(output['hostname']) != str(device['name']):
            r_connection.load_merge_candidate(config='hostname '+str(device['name']))
            compare = r_connection.compare_config()
            print(compare)
            r_connection.commit_config()
            #r_connection.discard_config()()
        r_connection.close()
    except Exception as err:
        print(err)
