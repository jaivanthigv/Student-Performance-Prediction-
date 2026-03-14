import pickle

model = pickle.load(open("models/model.pkl","rb"))

def predict_performance(study_hours,attendance,assignments,previous_score):

    data = [[study_hours,attendance,assignments,previous_score]]

    prediction = model.predict(data)

    return prediction[0]