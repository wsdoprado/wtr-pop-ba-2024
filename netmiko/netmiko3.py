#!/opt/intrarede/venv/bin/python3.10

import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

PE3 = {
    "device_type": "cisco_xr",
    "host": "192.168.246.96",
    "username": os.getenv("LAB_USERNAME"),
    "password": os.getenv("LAB_PASSWORD")
}

try: 
    pe3_connection = ConnectHandler(**PE3)

    print(pe3_connection.send_command('show running-config interface'))

    pe3_connection.disconnect()
    
except Exception as err:
    print(err)


