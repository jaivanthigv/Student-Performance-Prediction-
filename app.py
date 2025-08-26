from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model (ensure this path is correct)
model1 = pickle.load(open(r'student_performance_prediction.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')  # Form page

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from the form
    study_hours = float(request.form['study_hours'])
    attendance = float(request.form['attendance'])
    previous_grade = float(request.form['previous_grade'])

    # Prepare input for prediction
    input_data = np.array([[study_hours, attendance, previous_grade]])

    # Predict performance (you can use either predict or predict_proba depending on your model)
    prediction = model1.predict(input_data)[0]

    # Optionally: If using a classifier and want to apply threshold
    # prob = model1.predict_proba(input_data)[0][1]
    # performance = "Pass" if prob >= 0.7 else "Fail"

    # Send prediction to result template
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
