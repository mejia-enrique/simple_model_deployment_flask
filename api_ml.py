from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

# Loading the model
model = pickle.load(open('income_model.pkl', 'rb'))
with open('income_model.pkl', 'rb') as file:
    model.pickle.load(file)
print('Model loaded successfully...')

# Creating flask api that receives POST request
app = Flask(__name__)
@app.route('/api_predict_income', methods=['POST'])

def predict():
    # Get data from the POST request
    data = request.get_json(force=True)

    #Convert to a dataframe and enforce correct order
    try:
        input_data = pd.DataFrame(data)
        input_data = input_data[['education', 'years_of_experience', 'team_members']]
    except Exception as e:
        return jsonify({'Error': f"Error in the JSON format: {e}"}), 400

    # Predicting and showing the output
    prediction = model.predict(input_data)
    print(prediction)
    output = prediction.tolist()
    print(output)
    return jsonify(
        {'Income prediction': output}
    )

if __name__ == '__main__':
    # Host 0.0.0.0 to listed requests from any computer
    app.run(host='0.0.0.0' , port=8111, debug=True)