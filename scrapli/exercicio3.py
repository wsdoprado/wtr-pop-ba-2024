#!/opt/wtr-pop-ba-2024/venv/bin/python3.10

from scrapli_netconf.driver import NetconfDriver
import json, os, xmltodict
from dotenv import load_dotenv

load_dotenv()

router1 = {"host": "192.168.246.95","auth_username": os.getenv("LAB_USERNAME"),"auth_password": os.getenv("LAB_PASSWORD"), "port": 830}

try:
    with NetconfDriver(**router1) as conn:
        
        response = conn.get_config(source="running")
        
        xml_obj = response.result
        
        print(xml_obj)
        
        dict_obj = xmltodict.parse(xml_obj)
        
        print(dict_obj['rpc-reply']['data'])
        
        output_json = json.dumps(dict_obj['rpc-reply']['data'], indent=4)
        
        print(output_json)

        
except Exception as err:
    print(err)
    
    
