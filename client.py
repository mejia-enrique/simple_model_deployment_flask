import requests, json

# Parameters, getting the environment variables
IP = "192.168.1.224" # Second value is the default if not found 
PORT = "8111"
API_URL = f'http://{IP}:{PORT}/api_predict_income'

# Data to send
# education = 0:No degree, 1:Bachelors, 2:Masters, 3:Doctorate
#years_of_experience = Years of Experience as integer
#etam_members = 3  # Number of people in their team (direct and indirect reports)
data_to_send = [
    {"education": 1, "years_of_experience": 10, "team_members": 50},
    {"education": 2, "years_of_experience": 30, "team_members": 1}
                ]

# Sending request and receiving prediction
r = requests.post(API_URL, json=data_to_send)
print(r.json())