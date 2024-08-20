#!/opt/intrarede/venv/bin/python3.10

import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

PE3 = {
    "device_type": "huawei_vrp",
    "host": "192.168.50.2",
    "username": "williamp",
    "password": "212316Wsd@2020",
    'port': 2001,
}

try:
    pe3_connection = ConnectHandler(**PE3)

    print(pe3_connection.send_command("display interface brief"))

    pe3_connection.disconnect()

except Exception as err:
    print(err)


