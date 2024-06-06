# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

issue_id = input("Enter the issue id from which you want to get comments:\n")
url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/comment"
print(url)
auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

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
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
for i in range(data['total']):
    print(data["comments"][i]['body'])