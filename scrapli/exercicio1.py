#!/opt/wtr/venv/bin/python3.10

from scrapli.driver.core import IOSXRDriver
import os, json
from dotenv import load_dotenv

load_dotenv()

router1 = {"host": "192.168.246.95","auth_username": os.getenv("LAB_USERNAME"),"auth_password": os.getenv("LAB_PASSWORD")}

try:
    with IOSXRDriver(**router1) as conn:
        response = conn.send_command("show version")
        
        results = response.result
        
        print(results)
        
        results_textfsm = response.textfsm_parse_output()
        
        output_json = json.dumps(results_textfsm, indent=4)
        
        print(output_json)
except Exception as err:
    print(err)
    
    
