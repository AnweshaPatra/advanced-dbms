import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='database')

# Create a view of instructors without their salary called faculty
cursor = cnx.cursor()
cursor.execute("""
    CREATE OR REPLACE VIEW faculty AS
    SELECT ID, name, dept_name
    FROM instructors;
""")
cnx.commit()

# Create a view of department salary totals
cursor.execute("""
    CREATE OR REPLACE VIEW department_salary_totals AS
    SELECT dept_name, SUM(salary) AS total_salary
    FROM instructors
    GROUP BY dept_name;
""")
cnx.commit()

# Create a role of student
cursor.execute("""
    CREATE ROLE student;
""")
cnx.commit()

# Give select privileges on the view faculty to the role student
cursor.execute("""
    GRANT SELECT ON faculty TO student;
""")
cnx.commit()

# Create a new user and assign her the role of student
cursor.execute("""
    CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
""")
cnx.commit()

cursor.execute("""
    GRANT student TO 'newuser'@'localhost';
""")
cnx.commit()

# Revoke privileges of the new user
cursor.execute("""
    REVOKE SELECT ON faculty FROM 'newuser'@'localhost';
""")
cnx.commit()

# Remove the role of student
cursor.execute("""
    REVOKE student FROM 'newuser'@'localhost';
""")
cnx.commit()

cursor.execute("""
    DROP USER 'newuser'@'localhost';
""")
cnx.commit()

# Give select privileges on the view faculty to the new user
cursor.execute("""
    GRANT SELECT ON faculty TO 'newuser'@'localhost';
""")
cnx.commit()

# Close the connection
cnx.close()
