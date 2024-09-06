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


GRAPHQL_QUERY = {"query": f"""
{{
    device_list(
        filters: 
        {{
            id: 
            {{
                contains: "1"
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
    


device_interfaces_netbox = requests.post(url=url_graphql, json=GRAPHQL_QUERY, headers=headers, verify=False)
                 
print(device_interfaces_netbox.json())