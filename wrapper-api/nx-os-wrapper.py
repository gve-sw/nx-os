#
#   Cisco NX-API Wrapper API
#       v.01
#
#   
#   REQUIREMENTS:
#       Python requests library (issue the 'pip install requests' command in shell or cmd)
#
#   WARNING:
#       This script is meant for educational purposes only.
#       Any use of these scripts and tools is at
#       your own risk. There is no guarantee that
#       they have been through thorough testing in a
#       comparable environment and we are not
#       responsible for any damage or data loss
#       incurred with their use.
#

import requests

host = ''
username = ''
password = ''

class Wrapper_API(object):
    """
    This class is used to interact with the NX-API
    """
    def __init__(self):
        self.host = host
        self.username = username
        self.password = password

   def send_api_request(self, command):
        """
        Sends a request to the API for retrieving data.
        """
        url = 'http://' + host + '/ins' 
        myheaders={'content-type':'application/json-rpc'}
        payload=[
          {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {
              "cmd": command,
              "version": 1
            },
            "id": 1
          }
        ]
        return response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()


    def getInterface(self):
        """
        
        """
        devicesURL = ''
        apiRequest = Wrapper_API()
        response = apiRequest.send_api_request(devicesURL)

        interfaces = response['result']['body']['TABLE_interface']['ROW_interface']

        return interfaces

    def getResources(self):
        """
        
        """
        
        return apiResponse

    def getLicense(self):
        """
       
        """
        
        return apiResponse

    def getRoutes(self):
        """
       
        """
        
        return apiResponse

    def getIPMAC(self):
        """
       
        """
        
        return apiResponse