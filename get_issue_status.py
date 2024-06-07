# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

headers = {
    "Accept": "application/json"
 }
url = "https://nihallimbani05.atlassian.net/rest/api/2/search"
query = {
    'jql': 'project = DC'
}
response = requests.request(
    "GET",
    url,
    params=query,
    headers=headers,
    auth=auth
)
n = response.json()["total"]//100
all = []
for i in range(n+1):
    query = {
        'jql': 'project = DC',
        'startAt': i*100,
        'maxResults':100
    }
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query,             #Get all ID and Keys using pagination
        auth=auth
    )
    data = response.json()
    issues = data.get("issues",[])
    all.extend(issues)
    for row in all:
        print(row["id"],row["key"])
# for issue in data["issues"]:
    # issue_key = issue["key"]
    # new_url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/"+issue_key
    # response = requests.get(new_url, headers=headers, auth=auth)
    # data = response.json()
    # print(f"Issue id is {issue_key} and status is {data["fields"]["status"]["statusCategory"]["name"]}")

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
