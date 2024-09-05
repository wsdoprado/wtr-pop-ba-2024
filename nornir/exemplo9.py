from nornir import InitNornir
from nornir_netconf.plugins.tasks import netconf_get_config
import json,xmltodict

def nornir_task_wtr(task):
    data_interfaces = task.run(
    netconf_get_config, 
    source="running", 
    path="""
    <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
    </interface-configurations>""", 
    filter_type="subtree",
    )
    obj = xmltodict.parse(data_interfaces.result.rpc.data_xml)
    json_interfaces = json.loads(json.dumps(obj['data']))
    
    #print(json_interfaces['interface-configurations']['interface-configuration'])
    
    for interface in json_interfaces['interface-configurations']['interface-configuration']:
        print(interface)

nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 20}},
        inventory={
            "plugin": "NetBoxInventory2",
            "options": {
                "nb_url": "http://localhost:8000/",
                "nb_token": "c37c796a6b2155e4caa519b3ebb077b6f261dda8",
                "filter_parameters": {"region": ["salvador"],"status": "active", "platform": ["iosxr"]},
                "ssl_verify": False}
        })

nr.inventory.defaults.username = "wtr"
nr.inventory.defaults.password = "wtr"
nr.inventory.defaults.port = "830"

nr.run(task=nornir_task_wtr)



