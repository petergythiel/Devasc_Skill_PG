import requests
import datetime
import json
requests.packages.urllib3.disable_warnings()

DNAC_scheme = 'https://'
DNAC_authority = 'sandboxdnac.cisco.com'
DNAC_port = ':443'
DNAC_path_token = '/dna/system/api/v1/auth/token'
DNAC_path = '/dna/intent/api/v1/network-device'
DNAC_user = 'devnetuser'
DNAC_psw = 'Cisco123!'

#DATE AND TIME
print ("Current data en time: ")
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))

#TOKEN REQUEST
print("DEBUG: token request")
token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token

auth = (DNAC_user, DNAC_psw)
req = requests.request('POST', token_req_url, auth=auth, verify=False)
#print (req.status_code())
token = req.json()['Token']

#inventory request
print("DEBUG: inventory request")
req_url = DNAC_scheme + DNAC_authority + DNAC_port + DNAC_path
headers = {'X-AUTH-TOKEN': token}
resp_devices = requests.request('GET', req_url, headers = headers, verify = False)
resp_devices_json = resp_devices.json()

#Filter response DATA
print("DEBUG: Filter response DATA")
for device in resp_devices_json['response']:
    if device['type'] != None:
        print("===")
        #print(device)
        print("Hostname: " + device['hostname'])
        print("Familiy: " + device['family'])
        print("MAC: " + device['macAddress'])
        print("IP: " + device['managementIpAddress'])
        print("Software version: " + device['softwareVersion'])
        print("Reachability: " + device['reachabilityStatus'])