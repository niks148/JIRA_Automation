# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

issue_id = input("Enter the issue id in which you want to add attachment:\n")
url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/attachments"
print(url)
auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
    "Accept": "application/json",
    "X-Atlassian-Token": "no-check"
 }


response = requests.request(
    "POST",
    url,
    headers=headers,
    auth=auth,
    files = {
         "file": ("attach1.png", open("attach1.png","rb"), "application-type")
    }
)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
