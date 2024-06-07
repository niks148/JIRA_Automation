import requests
from requests.auth import HTTPBasicAuth
import json


auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
payload = json.dumps( {
    "timeSpentSeconds": 12000
  } )
for i in range(380,393):
  url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/DC-"+str(i)+"/worklog"
  print(url)
  response = requests.request(
     "POST",
     url,
     data=payload,
     headers=headers,
     auth=auth
  )
  print(response.text)
