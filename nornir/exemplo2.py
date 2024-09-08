#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

from nornir import InitNornir
from nornir_rich.functions import print_result
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command


nr = InitNornir(
    runner={"plugin": "threaded", "options": {"num_workers": 20}},
    config_file="hosts.yaml")

r1 = nr.filter(name="R1")

print_result(r1.run(netmiko_send_command, read_timeout=120, command_string="show interfaces brief"))


