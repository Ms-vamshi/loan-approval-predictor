from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('loan_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        applicantincome = float(request.form['applicantincome'])
        loanamount = float(request.form['loanamount'])
        credit_score = float(request.form['credit_score'])

        input_data = np.array([[applicantincome, loanamount, credit_score]])
        prediction = model.predict(input_data)

        result = "Loan Approved ✅" if prediction[0] == 1 else "Loan Denied ❌"
        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
