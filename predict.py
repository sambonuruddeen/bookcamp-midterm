import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'zindi_fi.bin'
vectorizer = 'dv.bin'

with open(model_file, 'rb') as f_in:
    
    dv, model = pickle.load(f_in)

#dv = pickle.load(open(vectorizer, 'rb'))
#print('Model Loaded')

app = Flask('Financial Inclusion')

customer = {"country": "Kenya",
            "year": 2018,
            "uniqueid": "uniqueid_6056",
            "location_type": "Urban",
            "cellphone_access": "Yes",
            "household_size": 3,
            "age_of_respondent": 30,
            "gender_of_respondent": "Male",
            "relationship_with_head": "Head of Household",
            "marital_status": "Married/Living together",
            "education_level": "Secondary education",
            "job_type": "Formally employed Government"
            }

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict(X)

    bank_account = y_pred

    result = {
        'Bank Account': bool(bank_account)

    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)