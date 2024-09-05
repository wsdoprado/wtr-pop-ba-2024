#!/opt/wtr/venv/bin/python3.10

import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

router1 = {"device_type": "cisco_xr","host": "192.168.246.95","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}

try:
    r1_connection = ConnectHandler(**router1)

    results = r1_connection.send_command('show ip int brief', use_textfsm=True)
    

    for interface in results:
        print(interface['interface'])

    r1_connection.disconnect()

except Exception as err:
    print(err)


