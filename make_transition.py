import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/DC-6/transitions"

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
   "transition": {
        "id": "4"
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

print(response.text)
