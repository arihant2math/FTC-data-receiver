import requests
import json

from requests.exceptions import InvalidSchema

WEB_SERVER = "192.168.43.1:7000"


def get_api_version():
    r = requests.get(WEB_SERVER)
    data = json.loads(r.text)
    return data["version"]


def get_logs():
    try:
        r = requests.get(WEB_SERVER + '/logs')
    except InvalidSchema:
        return {}
    data = json.loads(r.text)
    return data


def get_robot_position():
    try:
        r = requests.get(WEB_SERVER + '/robot-position')
    except InvalidSchema:
        return [0, 0]
    data = json.loads(r.text)
    return [data["x"], data["y"]]
