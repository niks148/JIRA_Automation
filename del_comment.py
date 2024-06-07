import requests
from requests.auth import HTTPBasicAuth

issue_id = input("Enter Issue ID from which you want to delete comments\n")
comment_id = input("Enter the comment_id\n")

url = "https://nihallimbani05.atlassian.net/rest/api/2/issue/" + issue_id + "/comment/" + comment_id


auth = HTTPBasicAuth("nihallimbani@gmail.com", "ATATT3xFfGF0BxjGsln6-RH5rfypUsHetu_lShRPhlaVvuUERKFhM_tnBgngqwlM202ly1uT6QuCWZojpSQMJOZoHFTFUhkmT15WRYFZfbVRXhaVvoSIjs3Sj8MD9UaUgxEp_JRIyT-6Udk44RF9Tng3gyFp1xhv96MgyvIh_7uFs86bx0MUSLM=7D71D18C")

response = requests.request(
    "DELETE",
    url,
    auth=auth
)

print(response.text)
