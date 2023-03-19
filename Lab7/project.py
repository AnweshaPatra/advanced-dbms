import mysql.connector

# connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database"
)

# create a cursor object to execute SQL commands
mycursor = mydb.cursor()

# create the info table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS info (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), contact_number VARCHAR(255))")

# prompt the user to enter their information
name = input("Enter your name: ")
address = input("Enter your address: ")
contact_number = input("Enter your contact number: ")

# insert the information into the info table
sql = "INSERT INTO info (name, address, contact_number) VALUES (%s, %s, %s)"
val = (name, address, contact_number)
mycursor.execute(sql, val)

# commit the changes to the database
mydb.commit()

# print a message to indicate that the information has been inserted
print(mycursor.rowcount, "record inserted.")
