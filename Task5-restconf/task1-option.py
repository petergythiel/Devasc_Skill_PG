import json
import requests
requests.packages.urllib3.disable_warnings()

#### Step 2: Create the variables that will be the components of the request
IP_ADDRESS = "192.168.56.101"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)


api_url = f"https://{IP_ADDRESS}/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"
headers = { "Accept": "application/yang-data+json",  "Content-type":"application/yang-data+json" }





#### Step 3: Create a variable to send the request and store the JSON response
resp = requests.options(api_url, auth=basicauth, headers=headers, verify=False)
print(resp.headers)
#print(dir(resp))

print(resp.status_code)
print("--------------1")
print(resp.headers)
print("--------------2")
print(resp.encoding)
print("--------------3")
#### Step 4: Format and display the JSON data received from the CSR1kv.
#response_json = resp.json()
#print(response_json)
#print(resp.status_code)
#print(json.dumps(response_json, indent=4))