#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

router1 = {"device_type": "cisco_xr","host": "192.168.246.95","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}

r1_connection = ConnectHandler(**router1)

results = r1_connection.send_command('show running-config interface', use_ttp=True, ttp_template="./template.ttp")

print(results)

print(f'type results: {type(results)}')

#finalizar a conexão com o PE1
r1_connection.disconnect()