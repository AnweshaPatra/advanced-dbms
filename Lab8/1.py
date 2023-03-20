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
cursor.execute("""CREATE FUNCTION calculate_q1_salary(jan_salary FLOAT, feb_salary FLOAT, mar_salary FLOAT)
RETURNS FLOAT
BEGIN
  DECLARE q1_salary FLOAT;
  SET q1_salary = jan_salary + feb_salary + mar_salary;
  RETURN q1_salary;
END;""")
cursor.execute("""SELECT calculate_q1_salary(1000.00, 1500.00, 2000.00) AS q1_salary;""")

# Close the cursor and database connection
cursor.close()
db.close()
