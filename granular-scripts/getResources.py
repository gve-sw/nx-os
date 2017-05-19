#!/usr/bin/python

import requests
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i','--ip',help='Switch IP address', required=True)
parser.add_argument('-p','--password',help='Switch Username', required=True)
parser.add_argument('-u','--user',help='Switch user', required=True)
args = parser.parse_args()

"""
Modify these please
"""

url='http://' +args.ip+ '/ins'
switchuser=args.user
switchpassword=args.password

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show hardware",
    "output_format": "json"
  }
}
try: 
   response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
   print "DEVICE NAME: " + json.dumps(response['ins_api']['outputs']['output']['body']['host_name'], indent=2, sort_keys=False).strip('"')
   print "VERSION: " + json.dumps(response['ins_api']['outputs']['output']['body']['kickstart_ver_str'], indent=2, sort_keys=False).strip('"')
   print "MEMORY: " + json.dumps(response['ins_api']['outputs']['output']['body']['memory'], indent=2, sort_keys=False) + json.dumps(response['ins_api']['outputs']['output']['body']['mem_type'], indent=2, sort_keys=False).strip('"')
   print "BOOTFLASH SIZE: " + json.dumps(response['ins_api']['outputs']['output']['body']['bootflash_size'], indent=2, sort_keys=False).strip('"')
   print "CHASSIS ID: " + json.dumps(response['ins_api']['outputs']['output']['body']['chassis_id'], indent=2, sort_keys=False).strip('"')
   print "CPU NAME: " + json.dumps(response['ins_api']['outputs']['output']['body']['cpu_name'], indent=2, sort_keys=False).strip('"')
except requests.exceptions.Timeout:
   print "time out for establishing connection"
except requests.exceptions.RequestException as e:
   print e 
   sys.exit(1)

