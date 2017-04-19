#!/usr/bin/python

import requests
import json
import argparse
import getpass
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i','--ip',help='Switch IP address', required=True)
parser.add_argument('-u','--user',help='Switch username', required=True)
args = parser.parse_args()

url='http://' +args.ip+ '/ins'

switchuser=args.user
switchpassword=getpass.getpass('Password:',stream=sys.stderr)

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show int brief ",
    "output_format": "json"
  }
}

try:
   response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
   print json.dumps(response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface'], indent=2, sort_keys=False)
except requests.exceptions.Timeout:
    # Maybe set up for a retry, or continue in a retry loop
    print "timed out connecting to device"
except requests.exceptions.RequestException as e:
    # catastrophic error. bail.
    print e
    sys.exit(1)



