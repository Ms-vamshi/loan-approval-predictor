import requests

data = {
    "income": 4500,
    "credit_score": 680,
    "loan_amount": 1300
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
