# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json


auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
f1 = open("bulk_assignee.csv",'r')
data=f1.read()
f1.close()

data = data.split("\n")[1:]

for row in data:
    issue_id = row.split(",")[0]
    acc_id = row.split(",")[1]
    url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/assignee"
    payload = json.dumps( {
      "accountId": acc_id
    } )
    response = requests.request(
       "PUT",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    print(response.text)
