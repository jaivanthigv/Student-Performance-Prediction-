import pandas as pd

data = {
    "study_hours":[5,2,6,3,7,4,1],
    "attendance":[80,50,90,60,95,70,40],
    "assignments":[8,4,9,5,10,6,3],
    "previous_score":[70,40,85,50,90,60,30],
    "final_result":["Pass","Fail","Pass","Fail","Pass","Pass","Fail"]
}

df = pd.DataFrame(data)

df.to_csv("students.csv",index=False)

print("CSV file created!")