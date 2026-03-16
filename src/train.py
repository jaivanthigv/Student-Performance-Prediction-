import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("data/students.csv")

X = data[["study_hours","attendance","assignments","previous_score"]]
y = data["result"]

# Split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train,y_train)

# Save model
with open("models/model.pkl","wb") as f:
    pickle.dump(model,f)

print("Model trained and saved!")