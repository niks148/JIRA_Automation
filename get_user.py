import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://nihallimbani05.atlassian.net/rest/api/2/users/search"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
