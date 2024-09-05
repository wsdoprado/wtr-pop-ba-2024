#!/opt/wtr/venv/bin/python3.10

import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

router1 = {"device_type": "cisco_xr","host": "192.168.246.95","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}

try:
    r1_connection = ConnectHandler(**router1)

    results1 = r1_connection.send_command('show ip int brief', use_textfsm=True)
    results2 = r1_connection.send_command('show version', use_textfsm=True)
    results3 = r1_connection.send_command('show arp', use_textfsm=True)
    results4 = r1_connection.send_command('ping 192.168.246.1', use_textfsm=True)
    
    print(results3)

    r1_connection.disconnect()

except Exception as err:
    print(err)


