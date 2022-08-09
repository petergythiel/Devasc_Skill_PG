import requests

 

access_token = "NGUwMmFkYjUtMTE0NS00NTRkLWFlZTYtMTI3YmYyMjFhN2Q3OTY0MmFiZDItZjdl_PF84_3f179706-f11a-4ab7-ba3e-57a4a96b089f"

#room_id = "Devasc_skills_PGY"
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vMjAzMWE5OTAtMTdkMi0xMWVkLWI5YzQtYWY4Yjg1YmIzYThk"

message = "URL Voor taak 1 op Github is : https://github.com/petergythiel/Devasc_Skill_PG"

url = "https://webexapis.com/v1/messages"

headers = {

    "Authorization": "Bearer {}".format(access_token),

    "Content-Type": "application/json"

}

params = {"roomId": room_id, "markdown": message}

res = requests.post(url, headers=headers, json=params)

print(res.json())