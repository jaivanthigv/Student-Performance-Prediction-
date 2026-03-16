import sqlite3

# connect to database
conn = sqlite3.connect("students.db")

cursor = conn.cursor()

# open SQL file
with open("database\students.sql", "r") as file:
    sql_script = file.read()

# execute SQL commands
cursor.executescript(sql_script)

conn.commit()

print("Table created and data inserted!")

conn.close()