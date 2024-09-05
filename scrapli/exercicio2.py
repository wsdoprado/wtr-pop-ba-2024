#!/opt/wtr/venv/bin/python3.10

from scrapli.driver.core import IOSXRDriver
import json, os
from dotenv import load_dotenv

load_dotenv()

router1 = {"host": "192.168.246.95","auth_username": os.getenv("LAB_USERNAME"),"auth_password": os.getenv("LAB_PASSWORD"), "transport": "telnet"}

try:
    with IOSXRDriver(**router1) as conn:
        response = conn.send_command("show version")
        print(response)
except Exception as err:
    print(err)
    
    
