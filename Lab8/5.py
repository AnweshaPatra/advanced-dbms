import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database"
)

# Create a function to check sabbatical eligibility and return instructor details
cursor = db.cursor()
cursor.execute("""
      CREATE FUNCTION check_sabbatical_eligibility(age INT)
      RETURNS VARCHAR(50)
      BEGIN
        DECLARE result VARCHAR(50);
          IF age > 40 THEN
          SET result = 'Eligible for sabbatical';
        ELSE
          SET result = 'Not eligible for sabbatical';
        END IF;
          RETURN result;
        END;
      """)

# Call the function to check if it has been successfully created
cursor.execute("SELECT check_sabbatical_eligibility(40)")

# Print the result
result = cursor.fetchone()
print(result[0])

# Close the database connection
db.close()
