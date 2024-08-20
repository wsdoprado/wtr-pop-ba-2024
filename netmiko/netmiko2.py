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
    "password": os.getenv("LAB_PASSWORD"),
}

try:
    pe3_connection = ConnectHandler(**PE3)

    commands = [
        "interface gigabitEthernet 0/0/0/1",
        "ipv4 address 192.168.100.1 255.255.255.252",
        "no shutdown",
    ]

    print(pe3_connection.send_config_set(commands))

    print(pe3_connection.commit())

    pe3_connection.disconnect()

except Exception as err:
    print(err)




