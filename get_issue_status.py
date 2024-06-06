# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

headers = {
    "Accept": "application/json"
 }
url = "https://nihallimbani05.atlassian.net/rest/api/2/search"
query = {
    'jql': 'project = DC',
    'maxResults':100
}
response = requests.request(
    "GET",
    url,
    params=query,
    headers=headers,
    auth=auth
)
# n = response.json()["total"]//100
# all = []
# for i in range(n+1):
#     query = {
#         'jql': 'project = DC',
#         'startAt': i*100,
#         'maxResults':100
#     }
#     response = requests.request(
#         "GET",
#         url,
#         headers=headers,
#         params=query,             #Get all ID and Keys using pagination
#         auth=auth
#     )
data = response.json()
#     issues = data.get("issues",[])
#     all.extend(issues)
#     for row in all:
#         print(row["id"],row["key"])
for issue in data["issues"]:
    issue_key = issue["key"]
    new_url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/"+issue_key
    response = requests.get(new_url, headers=headers, auth=auth)
    data = response.json()
    print(f"Issue id is {issue_key} and status is {data["fields"]["status"]["statusCategory"]["name"]}")

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
