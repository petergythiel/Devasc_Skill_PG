import requests
import json

 

access_token = "NGUwMmFkYjUtMTE0NS00NTRkLWFlZTYtMTI3YmYyMjFhN2Q3OTY0MmFiZDItZjdl_PF84_3f179706-f11a-4ab7-ba3e-57a4a96b089f"
url = "https://webexapis.com/v1/people/me"

headers = {

    "Authorization": "Bearer {}".format(access_token)

}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))


print("Deel 2: opzoeken van een gebruiker")
url = "https://webexapis.com/v1/people"

headers = {

    "Authorization": "Bearer {}".format(access_token),

    "Content-Type": "application/json"

}

params = {

    "email": ""

}

res = requests.get(url, headers=headers, params=params)

print(json.dumps(res.json(), indent=4))

print("Deel 3: alle rooms voor een gebruiker")

url = "https://webexapis.com/v1/rooms"

headers = {

    "Authorization": "Bearer {}".format(access_token),
    "Content-Type": "application/json"

}

params={"max": "100"}

res = requests.get(url, headers=headers, params=params)

print(res.json())

print("Deel 4: nieuwe  room voor een gebruiker")
url = "https://webexapis.com/v1/rooms"

headers = {

    "Authorization": "Bearer {}".format(access_token),

    "Content-Type": "application/json"

}

params={"title": "Devasc_skills_PGY"}

res = requests.post(url, headers=headers, json=params)

print(res.json())

print("Deel 5: recup van vorige code")



groups_struc = {
 "groups": [
      { "group": { "group_name": "Devasc_skills_PGY" ,    
                   "members": [   
                     {"person_name": "Peter", "email": "peter.gythiel@biasc.be"},
                     {"person_name": "PeterG", "email": "Peter.Gythiel@leraar.smi-aalst.be"},
                     {"person_name": "YvanR", "email": "Yvan.Rooseleer@biasc.be"} 
                   ]
                 }
      },
      { "group": { "group_name": "GROUP_NANO" ,    
                   "members": [   
                     {"person_name": "Peter", "email": "peter.gythiel@biasc.be"},
                     {"person_name": "PeterG", "email": "Peter.Gythiel@leraar.smi-aalst.be"} 
                   ]     
                 }
      }
   ]
}

url = "https://webexapis.com/v1/rooms"

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }

for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    if payload_space["title"] != None:  ### avoid errors if room title is unknown
        res_space = requests.post(url, headers=headers, json=payload_space)
        if res_space.status_code < 300: ### only create members if space has been created
            NEW_SPACE_ID = res_space.json()["id"]
            for mbr in rec["group"]["members"]:
                room_id = NEW_SPACE_ID
                person_email = mbr["email"] 
                url2 = 'https://webexapis.com/v1/memberships'
                payload_member = {'roomId': room_id, 'personEmail': person_email}
                res_member = requests.post(url2, headers=headers, json=payload_member)
