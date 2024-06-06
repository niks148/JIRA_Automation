import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/DC-328/worklog"

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "comment": {
    "content": [
      {
        "content": [
          {
            "text": "I did some work here.",
            "type": "text"
          }
        ],
        "type": "paragraph"
      }
    ],
    "type": "doc",
    "version": 1
  },
  "timeSpentSeconds": 12000
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
