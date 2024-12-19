import requests

def fetch_jwt_token(username, password):
    url = "http://127.0.0.1:8000/api/token/"
    data = {"username": username, "password": password}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=data, headers=headers)
    return response