import requests
import json

WEB_SERVER = "192.168.43.1:7000"


def get_api_version():
    r = requests.get(WEB_SERVER)
    data = json.loads(r.text)
    return data["version"]


def get_logs():
    r = requests.get(WEB_SERVER + '/logs')
    data = json.loads(r.text)
    return data
