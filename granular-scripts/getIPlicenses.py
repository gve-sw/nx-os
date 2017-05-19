#!/usr/bin/python

import requests
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-i','--ip',help='Switch IP address', required=True)
parser.add_argument('-p','--password',help='Switch Username', required=True)
parser.add_argument('-u','--user',help='Switch user', required=True)
args = parser.parse_args()

url='http://' +args.ip+ '/ins'
switchuser=args.user
switchpassword=args.password

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show license usage",
      "version": 1
    },
    "id": 1
  }
]
try:
   response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
   print "IP LICENCE:" +json.dumps(response['result']['body']['TABLE_show_lic_usage']['ROW_show_lic_usage'], indent=2, sort_keys=False)
except requests.exceptions.Timeout:
   print "time out for establishing connection"
except requests.exceptions.RequestException as e:
   print e 
   sys.exit(1)