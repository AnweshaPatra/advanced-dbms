import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database"
)

# Create a function to check sabbatical eligibility and return instructor details
def is_eligible_for_sabbatical(age):
  cursor = db.cursor()
  query = "SELECT * FROM instructor WHERE age > %s"
  cursor.execute(query, (age,))
  result = cursor.fetchall()
  cursor.close()
  return result

# Test the function
age = 40
instructors = is_eligible_for_sabbatical(age)
if len(instructors) > 0:
  print(f"Instructor(s) eligible for sabbatical with age > {age}:")
  for instructor in instructors:
    print(f"ID: {instructor[0]}, Name: {instructor[1]}, Department: {instructor[2]}, Salary: {instructor[3]}, Age: {instructor[4]}")
else:
  print(f"No instructor(s) eligible for sabbatical with age > {age}.")

# Close the database connection
db.close()
