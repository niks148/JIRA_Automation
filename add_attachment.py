# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

issue_id = input("Enter the issue id in which you want to add attachment:\n")
url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/attachments"
print(url)
auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

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
