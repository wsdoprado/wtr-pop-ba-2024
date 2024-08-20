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
    "fast_cli": "False"
}

pe3_connection = ConnectHandler(**PE3)


results = pe3_connection.send_command('show running-config interface', use_ttp=True, ttp_template="./template.ttp")

print(results)

#finalizar a conexão com o PE1
pe3_connection.disconnect()