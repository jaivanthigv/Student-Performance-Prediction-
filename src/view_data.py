import sqlite3
import pandas as pd

conn = sqlite3.connect("students.db")

# Show all students
data = pd.read_sql("SELECT * FROM students", conn)
print("\nAll Students")
print(data)

# Pass vs Fail count
pass_fail = pd.read_sql("""
SELECT result, COUNT(*) as total
FROM students
GROUP BY result
""", conn)

print("\nPass vs Fail")
print(pass_fail)

# Students who failed
failed_students = pd.read_sql("""
SELECT *
FROM students
WHERE result='Fail'
""", conn)

print("\nStudents Who Failed")
print(failed_students)

# Average attendance
avg_attendance = pd.read_sql("""
SELECT AVG(attendance) as average_attendance
FROM students
""", conn)

print("\nAverage Attendance")
print(avg_attendance)

conn.close()