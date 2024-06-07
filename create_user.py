# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

f = open("user_list.csv", 'r')
user_data = f.read()
f.close()

user_data = user_data.split("\n")[1:]

url = "https://nihallimbani05.atlassian.net/rest/api/2/user"

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
for users in user_data:
    email = users.split(",")[0]
    payload = json.dumps( 
        {
            "emailAddress":email,
            "products": ["jira-software"]
        }
    )
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
