#Taak 6 van restconf
#
import requests
requests.packages.urllib3.disable_warnings()

IP_HOST = "192.168.56.101"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"
DATA_FORMAT="application/yang-data+json"

api_url_put = f"https://{IP_HOST}/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

headers = { "Accept": DATA_FORMAT }
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)

resp_delete = requests.delete(api_url_put, auth=basicauth, headers=headers, verify=False)

print("----------------na delete")
print (resp_delete)
print("----------------na delete")
