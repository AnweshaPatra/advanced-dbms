import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='database')

# Create a table teaches2 with the same columns as teaches but with an additional constraint that
# the semester must be one of fall, winter, spring, or summer
cursor = cnx.cursor()
cursor.execute("""
    CREATE TABLE teaches2 (
        ID CHAR(5),
        course_id CHAR(8),
        sec_id CHAR(8),
        semester ENUM('Spring', 'Winter') NOT NULL,
        year INT,
        PRIMARY KEY (ID, course_id, sec_id, semester, year),
        FOREIGN KEY (ID) REFERENCES instructors(ID)
    );
""")
cnx.commit()

# Create an index on the ID column of the teaches table
cursor.execute("""
    CREATE INDEX teaches_ID_index ON teaches (ID);
""")
cnx.commit()

# Compare the difference in time to obtain query results with or without the index
# First, run the query without the index
cursor.execute("""
    SELECT * FROM teaches WHERE ID = '12345';
""")
result = cursor.fetchall()
print(result)

# Next, drop the index to free up the space
cursor.execute("""
    DROP INDEX teaches_ID_index ON teaches;
""")
cnx.commit()

# Close the connection
cnx.close()
