import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# Step 1: Create better-quality training data
data = {
    'applicantincome': [5000, 10000, 3000, 8000, 2000, 6000, 4000, 12000, 1500, 9000],
    'loanamount':      [1000, 4000, 5000, 6000, 2500, 3000, 5000, 7000, 2000, 8000],
    'credit_score':    [700, 750, 600, 720, 580, 680, 650, 800, 550, 730],
    'approved':        [1,    1,    0,    1,    0,   1,    0,    1,    0,   1]
}

df = pd.DataFrame(data)

# Step 2: Prepare data
X = df[['applicantincome', 'loanamount', 'credit_score']]
y = df['approved']

# Step 3: Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Step 4: Save the model
with open('loan_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as loan_model.pkl")
