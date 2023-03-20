# 1 . Given input as salary of three months (jan, feb, march), write a program that returns the total salary for quarter 1 (Q1).
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Retrieve the total salary for Q1
query = "SELECT SUM(salary) FROM instructors WHERE MONTH(NOW()) <= 3"
cursor.execute(query)
total_salary_q1 = cursor.fetchone()[0]

print("Total salary for Q1:", total_salary_q1)

# Close the cursor and database connection
cursor.close()
db.close()
