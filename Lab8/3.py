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

# Create the instructor table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS instructor (
  ID INT PRIMARY KEY,
  name VARCHAR(255),
  dept_name VARCHAR(255),
  salary INT,
  age INT
)
""")

# Add the tuples to the instructor table
tuples = [
  (10101, 'Srinivasan', 'Comp. Sci.', 65000, 34),
  (12121, 'Wu', 'Finance', 90000, 38),
  (15151, 'Mozart', 'Music', 40000, 45),
  (22222, 'Einstein', 'Physics', 95000, 55)
]
query = "INSERT INTO instructor (ID, name, dept_name, salary, age) VALUES (%s, %s, %s, %s, %s)"
cursor.executemany(query, tuples)
db.commit()

print("Tuples added successfully.")

# Close the cursor and database connection
cursor.close()
db.close()
