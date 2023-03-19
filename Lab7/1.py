import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='database')

# Create a view of instructors without their salary called faculty
cursor = cnx.cursor()
cursor.execute("""
    CREATE VIEW faculty AS
    SELECT ID, name, dept_name
    FROM instructors;
""")
cnx.commit()

# Create a view of department salary totals
cursor.execute("""
    CREATE VIEW dept_salary_totals AS
    SELECT dept_name, SUM(salary) AS total_salary
    FROM instructors
    GROUP BY dept_name;
""")
cnx.commit()

# Create a user and assign the role of student
cursor.execute("CREATE USER 'student' IDENTIFIED BY 'password'")
cnx.commit()

# Grant SELECT privileges on the view faculty to the user student
cursor.execute("GRANT SELECT ON faculty TO 'student'")
cnx.commit()

# Revoke privileges of the user
cursor.execute("REVOKE SELECT ON faculty FROM 'student'")
cnx.commit()

# Remove the role of student
cursor.execute("DROP USER 'student'")
cnx.commit()

# Give SELECT privileges on the view faculty to the new user
cursor.execute("GRANT SELECT ON faculty TO 'new_user'")
cnx.commit()

# Close the connection
cnx.close()
