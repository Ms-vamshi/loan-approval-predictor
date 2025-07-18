import requests

url = 'http://127.0.0.1:5000/predict_api'  # or '/predict' depending on your Flask route

data = {
    'gender': 1,
    'married': 1,
    'applicantincome': 5000,
    'loanamount': 150
}

res = requests.post(url, json=data)

print("Status Code:", res.status_code)
print("Response Text:", res.text)  # Debug: see actual server response
print("JSON Output:", res.json())  # Only if res.text is actually JSON
