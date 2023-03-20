import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database"
)

# Add columns to the instructor table
cursor = db.cursor()
add_columns_query = "ALTER TABLE instructor ADD COLUMN monthly_salary DECIMAL(10,2), ADD COLUMN exemptions DECIMAL(10,2), ADD COLUMN taxes DECIMAL(10,2), ADD COLUMN gross_salary DECIMAL(10,2)"
cursor.execute(add_columns_query)
db.commit()

# Update the new columns with calculated values
cursor.execute("SELECT * FROM instructor")
results = cursor.fetchall()

for result in results:
  salary = result[3]
  exemptions = salary * 0.1
  taxes = salary * 0.2
  monthly_salary = salary / 12
  gross_salary = salary - exemptions - taxes

  update_query = "UPDATE instructor SET monthly_salary=%s, exemptions=%s, taxes=%s, gross_salary=%s WHERE ID=%s"
  values = (monthly_salary, exemptions, taxes, gross_salary, result[0])
  cursor.execute(update_query, values)

db.commit()
cursor.close()

# Close the database connection
db.close()
