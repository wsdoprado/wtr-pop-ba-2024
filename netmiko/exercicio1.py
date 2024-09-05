#!/opt/wtr/venv/bin/python3.10

import os
from netmiko import ConnectHandler
from rich import print


#dict com os dados do device para acesso
router1 = {
    "device_type": "cisco_xr",
    "host": "192.168.246.95",
    "username": "wtr",
    "password": "wtr"
}

try:
    #conexão com o router1 e router2
    r1_connection = ConnectHandler(**router1)

    #executar o comando show version no router1 e router2 e mostrar o resultado
    results = r1_connection.send_command('show version')
    
    print(type(results))

    #finalizar a conexão com o router1 e router2
    r1_connection.disconnect()

except Exception as err:
    print(err)

