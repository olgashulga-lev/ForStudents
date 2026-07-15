import requests
import configparser
from pathlib import Path
from models import Player

config = configparser.ConfigParser()
config.read('config.ini')
BACKEND_URL = f"http://{config['DEFAULT']['BACKHOST']}:{config['DEFAULT']['BACKPORT']}/api"

def _make_request(method, endpoint, data=None, params=None):
    url = f"{BACKEND_URL}/{endpoint}"
    headers = {"Content-Type": "application/json"}
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers, params=params)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers, params=params)
        elif method == "DELETE":
            response = requests.delete(url, json=data, headers=headers, params=params)
        else:
            return None
        
        if response.status_code >= 400:
            print(f"Ошибка {response.status_code}: {response.text}")
            return None
        return response.json()
    except Exception as e:
        print(f"Ошибка запроса: {e}")
        return None

#Игроки 

