import requests, json

# Parameters
IP = '192.168.1.224'
PORT = '8111'
API_URL = f'http://{IP}:{PORT}/api_predict_income'

# Data to send for prediction
data_to_send = {"education": 3, "years_of_experience": 20, "team_members": 5}

# Dending request and receiving prediction
r = requests.post(API_URL, data_to_send)
print(r.json)