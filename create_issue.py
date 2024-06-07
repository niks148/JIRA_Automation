# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nihallimbani05.atlassian.net/rest/api/2/issue"

f1 = open("bulk_issue.csv",'r')
data=f1.read()
f1.close()

data = data.split("\n")[1:]
print(data)
auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

for rows in data:
   payload = json.dumps( 
   {
      "fields": {
        "assignee": {
          "id": rows.split(",")[0]
        },
        "description": rows.split(",")[1],
        "issuetype": {
          "id": rows.split(",")[2]
        },
        "parent": {
          "key": "DC-332"
        },
        "priority": {
          "id": rows.split(",")[3]
        },
        "project": {
          "id": "10001"
        },
        "reporter": {
          "id": rows.split(",")[4]
        },
        "summary": rows.split(",")[5],
        "timetracking": {
          "originalEstimate": "10h",
          "remainingEstimate": "8h"
        }
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

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))