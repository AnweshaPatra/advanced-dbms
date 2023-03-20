import mysql.connector
import random

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Alter the existing instructor table
query1 = "ALTER TABLE instructors ADD age INT;"
cursor.execute(query1)
db.commit()

# Generate a random age between 30 and 50 for each instructor
for id in range(1, 153): 
    age = random.randint(30, 50)
    query = "UPDATE instructors SET age = %s"
    values = (age, id)
    cursor.execute(query, values)
    db.commit()

print("Age updated successfully.")

# Close the cursor and database connection
cursor.close()
db.close()
