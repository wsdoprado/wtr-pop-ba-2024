#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

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