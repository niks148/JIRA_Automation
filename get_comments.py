# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

issue_id = input("Enter the issue id from which you want to get comments:\n")
url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/comment"
print(url)
auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
    "Accept": "application/json"
 }


response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)
data = response.json()
for i in range(data['total']):
    print(data["comments"][i]['body'])