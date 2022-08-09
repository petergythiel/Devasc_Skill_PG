from requests_toolbelt import MultipartEncoder
import requests

access_token = "NGUwMmFkYjUtMTE0NS00NTRkLWFlZTYtMTI3YmYyMjFhN2Q3OTY0MmFiZDItZjdl_PF84_3f179706-f11a-4ab7-ba3e-57a4a96b089f"

#room_id = "Devasc_skills_PGY"
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vMjAzMWE5OTAtMTdkMi0xMWVkLWI5YzQtYWY4Yjg1YmIzYThk"

filepath    = '/home/devasc/Devasc_Skills/Devasc_Skill_PG/pictures/Task1-GITHUB.png'
filetype    = 'image/png'
#roomId      = 'SOME ROOM'
#token       = 'YOUR ACCOUNT BEARER TOKEN'
url         = "https://webexapis.com/v1/messages"
token = access_token

my_fields={'roomId': room_id, 
           'text': 'DevAsc - Taak 1 = GIT configuratie',
           'files': ('screenshot', open(filepath, 'rb'), filetype)
           }
m = MultipartEncoder(fields=my_fields)
#r = requests.post(url, data=m,
#                  headers={'Content-Type': m.content_type,
#                           'Authorization': 'Bearer ' + token})
#print (r.json())

#2de foto
filepath    = '/home/devasc/Devasc_Skills/Devasc_Skill_PG/pictures/Taak 10- DNAC.png'
filetype    = 'image/png'
my_fields={'roomId': room_id, 
           'text': 'DevAsc - Taak 10 = DNAC configuratie',
           'files': ('screenshot', open(filepath, 'rb'), filetype)
           }
m = MultipartEncoder(fields=my_fields)
r = requests.post(url, data=m,
                  headers={'Content-Type': m.content_type,
                           'Authorization': 'Bearer ' + token})
print (r.json())

