import pandas as pd
import random

data = []

for i in range(1000):

    study_hours = random.randint(1,10)
    attendance = random.randint(40,100)
    assignments = random.randint(1,10)
    previous_score = random.randint(30,100)

    if previous_score >= 50:
        result = "Pass"
    else:
        result = "Fail"

    data.append([
        study_hours,
        attendance,
        assignments,
        previous_score,
        result
    ])

df = pd.DataFrame(data, columns=[
    "study_hours",
    "attendance",
    "assignments",
    "previous_score",
    "result"
])

df.to_csv("data/students.csv", index=False)

print("Random dataset created successfully!")