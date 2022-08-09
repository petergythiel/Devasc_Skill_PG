import requests
import json


groups_struc = {
 "groups": [
      { "group": { "group_name": "Devasc_skills_PGY" ,    
                   "members": [   
                     {"person_name": "Peter", "email": "peter.gythiel@biasc.be"},
                     {"person_name": "PeterG", "email": "Peter.Gythiel@leraar.smi-aalst.be"},
                     {"person_name": "Peter_G", "email": "Peter_Gythiel@hotmail.com"} 
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




access_token = "b3c5b2e9-1d70-403f-8f2b-6ac1d0ab870c"
url = 'https://api.ciscospark.com/v1/rooms'
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
                url2 = 'https://api.ciscospark.com/v1/memberships'
                payload_member = {'roomId': room_id, 'personEmail': person_email}
                res_member = requests.post(url2, headers=headers, json=payload_member)




{
  "title": "Project Unicorn - Sprint 0",
  "teamId": "Y2lzY29zcGFyazovL3VzL1JPT00vNjRlNDVhZTAtYzQ2Yi0xMWU1LTlkZjktMGQ0MWUzNDIxOTcz",
  "classificationId": "Y2lzY29zcGFyazovL3VzL0NMQVNTSUZJQ0FUSU9OL2YyMDUyZTgyLTU0ZjgtMTFlYS1hMmUzLTJlNzI4Y2U4ODEyNQ",
  "isLocked": false,
  "isAnnouncementOnly": false
}



###  DELETE WEBEX "DEMO" SPACES
from webexteamssdk import WebexTeamsAPI
### Access Token 12 hours: https://developer.webex.com/docs/api/getting-started (login required)
access_token = "NGUwMmFkYjUtMTE0NS00NTRkLWFlZTYtMTI3YmYyMjFhN2Q3OTY0MmFiZDItZjdl_PF84_3f179706-f11a-4ab7-ba3e-57a4a96b089f"
api = WebexTeamsAPI(access_token=access_token)
# Find all rooms that should be removed
all_rooms = api.rooms.list()
print ("All rooms", all_rooms)
demo_rooms = [room for room in all_rooms if 'GROUP_NANO' in room.title]

# Delete all of the demo rooms
for room in demo_rooms:
    print("Deleting ... " + room.title)
    api.rooms.delete(room.id)