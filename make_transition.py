import requests
from requests.auth import HTTPBasicAuth
import json

issue_id = input("Enter the issue_id on which you want to make transition:\n")
url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/transitions"

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# payload = json.dumps({
#    "transition": {
#         "id": "4"
#     }
# }
# )
payload = json.dumps(
    {
      "update": {
          "comment": [
              {
                  "add": {
                      "body": "Bug has been fixed."
                  }
              }
          ]
      },
      "transition": {
          "id": "5"
      }
}  
)

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(response.text)
