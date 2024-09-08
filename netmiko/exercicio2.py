#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
from rich import print

#carregar as variáveis definidas no .env
load_dotenv()

#dict com os dados do device para acesso
router1 = {"device_type": "cisco_xr","host": "192.168.246.95","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}
router2 = {"device_type": "cisco_xr","host": "192.168.246.96","username": os.getenv("LAB_USERNAME"),"password": os.getenv("LAB_PASSWORD")}

try:
    #conexão com o router1 e router2
    r1_connection = ConnectHandler(**router1)
    r2_connection = ConnectHandler(**router2)

    #executar o comando show version no router1 e router2 e mostrar o resultado
    print(r1_connection.send_command('show version'))
    print(r2_connection.send_command('show version'))

    #finalizar a conexão com o router1 e router2
    r1_connection.disconnect()
    r2_connection.disconnect()

except Exception as err:
    print(err)





