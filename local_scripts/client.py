import requests, json

# Parameters
#IP = "192.168.1.224"
#PORT = "8111"
RENDER_URL = 'https://simple-model-deployment-flask.onrender.com'
API_URL = f'{RENDER_URL}/api_predict_income'

# Data to send
# education = 0:No degree, 1:Bachelors, 2:Masters, 3:Doctorate
#years_of_experience = Years of Experience as integer
#etam_members = 3  # Number of people in their team (direct and indirect reports)
data_to_send = [
    {"education": 0, "years_of_experience": 0, "team_members": 0},
    {"education": 2, "years_of_experience": 10, "team_members": 20},
    {"education": 3, "years_of_experience": 20, "team_members": 60}
                ]

# Sending request and receiving prediction
r = requests.post(API_URL, json=data_to_send)
print(r.json())