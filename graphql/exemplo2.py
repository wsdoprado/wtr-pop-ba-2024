#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

from nornir import InitNornir 
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
    
    device_interfaces_netbox = requests.post(url=url_graphql, json=GRAPHQL_QUERY, headers=headers, verify=False).json()['data']['device_list'][0]['interfaces']
    print(device_interfaces_netbox)
                 
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

 