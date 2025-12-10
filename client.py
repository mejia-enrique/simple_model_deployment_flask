import requests, json

# Data to send
education = 1  # 0:No degree, 1:Bachelors, 2:Masters, 3:Doctorate
yoe = 10 #Years of Experience as integer
team_members = 3  # Number of people in their team (direct and indirect reports)

# Parameters
IP = '192.168.1.224'
PORT = '8111'
API_URL = f'http://{IP}:{PORT}/api_predict_income'

# Data to send for prediction (a list of dictionaries)
data_to_send = [
    {"education": education, "years_of_experience": yoe, "team_members": team_members},
    {"education": 2, "years_of_experience": 3, "team_members": 1}
                ]

# Sending request and receiving prediction
r = requests.post(API_URL, json=data_to_send)
print(r.json())