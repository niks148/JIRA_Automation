# JIRA_Automation
This repository helps end-user to do basic operations like create Task, Bug, Epic, bulk user and so on. This code also allows user to comment on particular issue using issue_id and attach particular file to particular issue using issue_id. 

## This repo provides the following functionalities:
* Create single user or bulk user
* Create single issue or bulk issue of any type(Task, Bug, Epic)
* Make Comments on particular issue
* Delete comment on particular issue
* Log the time hours on particular issue
* Attach the file to particular issue
* Make status transition of particular issue

## Requirements

- Python version 3.6^
- Jira cloud instance with API Token

**Note:** The user will be able to perform actions on the API as per permission level, if for example, user doesn't have permissions to create new projects in JIRA, he will be not able to do it using the API token too. This means that in some cases he will need to ask someone to provide the API token with more access — depends on the integration.
