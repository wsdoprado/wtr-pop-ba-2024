#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

load_dotenv()

router1 = {"device_type": "cisco_xr","host": "192.168.246.95","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}
router2 = {"device_type": "cisco_xr","host": "192.168.246.96","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}

try:
    #conexão com o router1 e router2
    r1_connection = ConnectHandler(**router1)
    r2_connection = ConnectHandler(**router2)

    commands_router1 = ["interface gigabitEthernet 0/0/0/1","ipv4 address 192.168.100.1 255.255.255.252","no shutdown"]
    commands_router2 = ["interface gigabitEthernet 0/0/0/1","ipv4 address 192.168.100.2 255.255.255.252","no shutdown"]
    
    #enviar a lista de comandos para o router1 e realizar o commit
    print(r1_connection.send_config_set(commands_router1))
    print(r1_connection.commit())

    #enviar a lista de comandos para o router2 e realizar o commit
    print(r2_connection.send_config_set(commands_router2))
    print(r2_connection.commit())

    #finalizar a conexão com o router1 e router2
    r1_connection.disconnect()
    r2_connection.disconnect()

except Exception as err:
    print(err)


