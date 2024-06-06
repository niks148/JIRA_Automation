# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

f = open("user_list.csv", 'r')
user_data = f.read()
f.close()

user_data = user_data.split("\n")[1:]

url = "https://nihallimbani05.atlassian.net/rest/api/2/user"

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
for users in user_data:
    email = users.split(",")[0]
    payload = json.dumps( 
        {
            "emailAddress":email,
            "products": ["jira-software"]
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
