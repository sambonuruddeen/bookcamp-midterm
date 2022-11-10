#!/usr/bin/env python
# coding: utf-8

import requests

url = "http://127.0.0.1:9696/predict"


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

response = requests.post(url, json=customer).json()


print(response)

if (response['Bank Account'] == True):
    print("The customer has an account")
else:
    print("The customer has no account")


