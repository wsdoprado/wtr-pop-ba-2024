#!/opt/wtr/venv/bin/python3.10

from nornir import InitNornir
from nornir_rich.functions import print_result     
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config, netmiko_commit
from nornir_napalm.plugins.tasks import napalm_get

import requests

url_graphql = "http://localhost:8000/graphql/"
token = "c37c796a6b2155e4caa519b3ebb077b6f261dda8"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token '+token
}

def nornir_task_wtr(task):
    device = nr.inventory.hosts[task.host.name]
    device_id = device['id']
    GRAPHQL_QUERY = {"query": f"""
    {{
        device_list(
            filters: 
            {{
                id: 
                {{
                    contains: {device_id}
                }}
            }}
        )
    {{
        name
        primary_ip4
        {{
            address
        }}
        platform
        {{
            name
        }}
        status
        interfaces
        {{
            name
            description
            mtu
            enabled
            ip_addresses
            {{
                address
            }}
        }}
    }}
    }}"""}
    
    data_device = task.run(napalm_get, getters=["get_interfaces"])
    data_device = data_device.result['get_interfaces']

    device_interfaces_netbox = requests.post(url=url_graphql, json=GRAPHQL_QUERY, headers=headers, verify=False).json()['data']['device_list'][0]['interfaces']

    for interface_netbox in device_interfaces_netbox:
        interface_name_netbox = interface_netbox['name']
        interface_description_netbox = interface_netbox['description']
        interface_status_netbox = interface_netbox['enabled']
        interface_mtu_netbox = interface_netbox['mtu']
        if data_device[interface_name_netbox]:
            interface_description_device =  data_device[interface_name_netbox]['description']
            interface_status_device = data_device[interface_name_netbox]['is_enabled']
            interface_mtu_device = data_device[interface_name_netbox]['mtu']

            configurations=["interface "+str(interface_netbox['name'])]
            if interface_status_device != interface_status_netbox:
                if interface_status_netbox == True:
                    configurations.append("no shutdown")
                if interface_status_netbox == False:
                    configurations.append("shutdown")
                    
            if interface_description_device != interface_description_netbox:
                if interface_description_netbox == "":
                    configurations.append("no description")
                else:        
                    configurations.append("description "+str(interface_description_netbox))
                    
            if interface_mtu_device != interface_mtu_netbox:
                if interface_mtu_netbox != None:
                    configurations.append("mtu "+str(interface_mtu_netbox))
                
            if len(configurations) > 1:
                command = task.run(netmiko_send_config, config_commands=configurations)
                print_result(command)
                commit = task.run(netmiko_commit)
                print_result(commit)

                    
nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 20}},
        inventory={
            "plugin": "NetBoxInventory2",
            "options": {
                "nb_url": "http://localhost:8000/",
                "nb_token": "c37c796a6b2155e4caa519b3ebb077b6f261dda8",
                "filter_parameters": {"region": ["salvador","belohorizonte"],"status": "active", "platform": ["iosxr"]},
                "ssl_verify": False}
        })

nr.inventory.defaults.username = "wtr"
nr.inventory.defaults.password = "wtr"
nr.inventory.defaults.port = "22"

nr.run(task=nornir_task_wtr)

 