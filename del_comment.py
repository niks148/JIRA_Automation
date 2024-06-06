import requests
from requests.auth import HTTPBasicAuth
import json
issue_id = input("Enter Issue ID from which you want to delete comments\n")
comment_id = input("Enter the comment_id\n")

url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/comment/" + comment_id


auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0ftqZEU1AVIi3voauaZpx_plob-fWDKt9tQUL4GfxpgnhEkYPyFW8P-O-tuYMYZRXLQLbe5VG3pT-0GzrdYNTvkHeU8yh-eDpTYVjbYSb_08qRSSYQ2Y5kY9Rg2SPazpAF2OE1wAWVs5LEszQWBqmp7Qn6ELkR74eQWl2XcGQPHs=88883CCD")

response = requests.request(
    "DELETE",
    url,
    auth=auth
)

print(response.text)
