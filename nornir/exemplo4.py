#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(
        runner={"plugin": "threaded", "options": {"num_workers": 20}},
        inventory={
            "plugin": "NetBoxInventory2",
            "options": {
                "nb_url": "http://localhost:8000/",
                "nb_token": "c37c796a6b2155e4caa519b3ebb077b6f261dda8",
                "ssl_verify": False}
        })

nr.inventory.defaults.username = "wtr"
nr.inventory.defaults.password = "wtr"
nr.inventory.defaults.port = "22"


print(nr.inventory.hosts)

print(nr.inventory.hosts['ncs5501-popba-95'].data)

