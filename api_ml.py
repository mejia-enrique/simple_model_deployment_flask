from flask import Flask
import requests, jsonify
import pickle
import pandas as pd
import numpy as np

# Loading the model
model = pickle.load('income_model.pkl', 'rb')

# Creating flask api that receives POST requests
app = Flask(__name__)
@app.route('/api_predict_income', methods=['POST'])

def predict():
    # Get data from the POST request
    data = requests.get_json(force=True)
    predict_request = [[
            data['educuation'],
            data['years_of_experience'],
            data['team_members']
            ]]
    print('Predict Request list of lists', predict_request)
    predict_request=np.array(predict_request)
    print('Predict Request numpy array', predict_request)
    prediction = model.predict(predict_request)
    print(prediction)
    # Taking the first value of the prediction
    output=prediction[0]
    print(output)
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=8111, debug=True)