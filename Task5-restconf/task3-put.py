#Taak 3 van restconf
#
import requests
requests.packages.urllib3.disable_warnings()

IP_HOST = "192.168.56.101"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"

api_url_put = f"https://{IP_HOST}/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

headers = { "Accept": DATA_FORMAT ,  "Content-type": DATA_FORMAT }
#headers = { "Accept": DATA_FORMAT ,  "Content-type": DATA_FORMAT , "severity": "warnings"}
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)
payload = { "severity": "warnings" }

#resp_put = requests.put(api_url_put, data=payload, auth=basicauth, headers=headers, verify=False)
resp_put = requests.put(api_url_put, auth=basicauth, headers=headers, verify=False)

print("----------------na put")
print (resp_put)
print("----------------na print")


if resp_put.status_code in range(200,300):
    print(f"STATUS OK: {resp_put.status_code}") 
else:
    print("ERROR") 
    print(resp_put.status_code)
    print(resp_put.text)
