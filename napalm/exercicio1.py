#!/opt/wtr/venv/bin/python3.10

from napalm import get_network_driver
import json, os
from dotenv import load_dotenv

load_dotenv()

driver = get_network_driver('iosxr')

router1 = {"hostname": "192.168.246.95","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}

try:
    r1_connection = driver(**router1)
    r1_connection.open()
    print(f"Connecting to {router1['hostname']}")
    #output = r1_connection.get_interfaces() 
    output = r1_connection.get_facts() 
    #output = r1_connection.get_interfaces_ip() 
    #output = r1_connection.get_interfaces_counters() 
    r1_connection.close()

    output_json = json.dumps(output, indent=4)
    print(output_json)
except Exception as err:
    print(err)
    
    
