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

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

for rows in data:
   payload = json.dumps( 
       {
           "fields": {
              "project":
              {
                 "key": rows.split(",")[0]
              },
              "summary": rows.split(",")[2],
              "description": rows.split(",")[1],
              "issuetype": {
                 "name": rows.split(",")[3]
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