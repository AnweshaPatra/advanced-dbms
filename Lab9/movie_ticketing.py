import mysql.connector
import os

# Connect to the database
db = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'database')

# Create a cursor object to interact with the database
cursor = db.cursor()


class Movie:
    def _init_(self, name, release_date, director, cast, description):
        self.name = name
        self.release_date = release_date
        self.director = director
        self.cast = cast
        self.description = description

    def save(self):
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database="movie_booking"
        )
        cursor = conn.cursor()
        query = "INSERT INTO movies (name, release_date, director, cast, description) VALUES (%s, %s, %s, %s, %s)"
        values = (self.name, self.release_date, self.director, self.cast, self.description)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

class Theater:
    def _init_(self, name, city):
        self.name = name
        self.city = city

    def save(self):
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database="movie_booking"
        )
        cursor = conn.cursor()
        query = "INSERT INTO theaters (name, city) VALUES (%s, %s)"
        values = (self.name, self.city)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

class Screen:
    def _init_(self, name, theater_id):
        self.name = name
        self.theater_id = theater_id

    def save(self):
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database="movie_booking"
        )
        cursor = conn.cursor()
        query = "INSERT INTO screens (name, theater_id) VALUES (%s, %s)"
        values = (self.name, self.theater_id)
        cursor.execute(query, values)
        conn.commit()
        conn.close()


class Booking:
    def init(self, movie_id, theater_id, screen_id, user_name, booking_time):
        self.movie_id = movie_id
        self.theater_id = theater_id
        self.screen_id = screen_id
        self.user_name = user_name
        self.booking_time = booking_time
    def save(self):
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database="movie_booking"
        )
        cursor = conn.cursor()
        query = "INSERT INTO bookings (movie_id, theater_id, screen_id, user_name, booking_time) VALUES (%s, %s, %s, %s, %s)"
        values = (self.movie_id, self.theater_id, self.screen_id, self.user_name, self.booking_time)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
    def cancel(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="movie_booking"
        )
        cursor = conn.cursor()
        query = "DELETE FROM bookings WHERE movie_id = %s AND theater_id = %s AND screen_id = %s AND user_name = %s AND booking_time = %s"
        values = (self.movie_id, self.theater_id, self.screen_id, self.user_name, self.booking_time)
        cursor.execute(query, values)
        conn.commit()
        conn.close()

def view_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="movie_booking"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()


def main():
    print("Welcome to the movie booking system.")
    while True:
        print("Please choose an option:")
        print("1. Add movie")
        print("2. Add theater")
        print("3. Add screen")
        print("4. Book ticket")
        print("5. Cancel ticket")
        print("6. View data")
        print("7. Quit")

        choice = input()

        if choice == "1":
            name = input("Enter movie name: ")
            release_date = input("Enter release date (YYYY-MM-DD): ")
            director = input("Enter director name: ")
            cast = input("Enter cast members (comma separated): ")
            description = input("Enter movie description: ")
            movie = Movie(name, release_date, director, cast, description)
            movie.save()
            print("Movie added successfully.")
        elif choice == "2":
            name = input("Enter theater name: ")
            city = input("Enter city name: ")
            theater = Theater(name, city)
            theater.save()
            print("Theater added successfully.")
        elif choice == "3":
            name = input("Enter screen name: ")
            theater_id = input("Enter theater ID: ")
            screen = Screen(name, theater_id)
            screen.save()
            print("Screen added successfully.")
        elif choice == "4":
            movie_id = input("Enter movie ID: ")
            theater_id = input("Enter theater ID: ")
            screen_id = input("Enter screen ID: ")
            user_name = input("Enter user name: ")
            booking_time = input("Enter booking time (YYYY-MM-DD HH:MM:SS): ")
            booking = Booking(movie_id, theater_id, screen_id, user_name, booking_time)
            booking.save()
            print("Booking successful.")
        elif choice == "5":
            movie_id = input("Enter movie ID: ")
            theater_id = input("Enter theater ID: ")
            screen_id = input("Enter screen ID: ")
            user_name = input("Enter user name: ")
            booking_time = input("Enter booking time (YYYY-MM-DD HH:MM:SS): ")
            booking = Booking(movie_id, theater_id, screen_id, user_name, booking_time)
            booking.cancel()
            print("Booking cancelled successfully.")
        elif choice == "6":
            view_data()
        elif choice == "7":
            print("Thank you for using the movie booking system.")
            break
        else:
            print("Invalid choice. Please try again.")


main()


    
       
cursor.execute('''
CREATE DATABASE IF NOT EXISTS movie_booking;

USE movie_booking;

CREATE TABLE  IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    release_date DATE NOT NULL,
    director VARCHAR(255) NOT NULL,
    cast VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS theaters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
);

    name VARCHAR(255) NOT NULL,
    theater_id INT NOT NULL,
    FOREIGN KEY (theater_id) REFERENCES theaters(id)
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT NOT NULL,
    theater_id INT NOT NULL,
    screen_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    booking_time DATETIME NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (theater_id) REFERENCES theaters(id),
    FOREIGN KEY (screen_id) REFERENCES screens(id)
);''')