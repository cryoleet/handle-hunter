import sys
import json
import requests


username = sys.argv[1]


with open("sites.json") as data_json:
    data = json.load(data_json)



for site, details in data.items():

    response = requests.get(details["url"].replace("{}", username))

    if details["checkType"] == "status_code":

        if response.status_code == 200:
            print(f"{site} : {details['url'].replace('{}', username)}")

    elif details["checkType"] == "message":

        if details["message"] not in response.text:
            print(f"{site} : {details['url'].replace('{}', username)}")


