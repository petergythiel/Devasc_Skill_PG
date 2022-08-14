#Taak 2 van restconf
#
import requests
requests.packages.urllib3.disable_warnings()

IP_HOST = "192.168.56.101"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"

api_url_post = f"https://{IP_HOST}/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

headers = { "Accept": DATA_FORMAT ,  "Content-type": DATA_FORMAT }
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)
payload = { "severity": "alerts" }
payload = {
    "severity": "alerts"
}

#resp_put = requests.put(api_url_put, data=payload, auth=basicauth, headers=headers, verify=False)
resp_post = requests.post(api_url_post, json=payload, auth=basicauth, headers=headers, verify=False)

print("----------------na post")
print (resp_post)
print("----------------na print")

