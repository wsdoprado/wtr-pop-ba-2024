from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_config, netmiko_commit

def nornir_task_wtr(task):
    configurations = ["hostname "+str(task.host.name)]
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
                "filter_parameters": {"region": ["salvador"],"status": "active", "platform": ["iosxr"]},
                "ssl_verify": False}
        })

nr.inventory.defaults.username = "wtr"
nr.inventory.defaults.password = "wtr"
nr.inventory.defaults.port = "22"

nr.run(task=nornir_task_wtr)



