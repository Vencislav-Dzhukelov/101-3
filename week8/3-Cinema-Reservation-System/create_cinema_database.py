import sqlite3


class CreateCinemaDB():

    def make_db(self):
        db = sqlite3.connect("movie_database.db")
        cursor = db.cursor()

        create_table_movies = '''CREATE TABLE IF NOT EXISTS Movies(
                    id INTEGER PRIMARY KEY,
                    name TEXT, rating REAL)'''

        create_table_projections = '''CREATE TABLE IF NOT EXISTS Projections(
                    id INTEGER PRIMARY KEY,movie_id INTEGER,
                    type TEXT, date TEXT, time TEXT,
                    FOREIGN KEY(movie_id) REFERENCES Movies(id))'''

        create_table_reservations = '''CREATE TABLE IF NOT EXISTS Reservations(
                    id INTEGER PRIMARY KEY, username TEXT,
                    projection_id INTEGER, row INTEGER, col INTEGER,
                    FOREIGN KEY(projection_id) REFERENCES Projections(id))'''

        cursor.execute(create_table_movies)
        cursor.execute(create_table_projections)
        cursor.execute(create_table_reservations)

    def add_movie(self, new_name, new_rating):
        db = sqlite3.connect("movie_database.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO Movies(name, rating)\
                        VALUES (?, ?)", (new_name, new_rating))
        db.commit()
        db.close()

    def add_projection(self, movie_id, type, date, time):
        db = sqlite3.connect("movie_database.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO Projections(movie_id, type, date, time)\
                        VALUES (?, ?, ?, ?)",
                       (movie_id, type, date, time))
        db.commit()
        db.close()

    def add_reservations(self, username, projection_id, row, col):
        db = sqlite3.connect("movie_database.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO Reservations(username, projection_id, row, col)\
                        VALUES (?, ?, ?, ?)",
                       (username, projection_id, row, col))
        db.commit()
        db.close()

c = CreateCinemaDB()
if __name__ == "__main__":
    # c.make_db()
    c.add_movie("The Hunger Games: Catching Fire", 7.9)
    c.add_movie("Wreck-It Ralph", 7.8)
    c.add_movie("Her", 8.3)
    c.add_projection(1, "3D", "2014-04-01", "19:10")
    c.add_projection(1, "2D", "2014-04-01", "19:00")
    c.add_projection(1, "4DX", "2014-04-02", "21:00")
    c.add_projection(3, "2D", "2014-04-05", "20:20")
    c.add_projection(2, "3D", "2014-04-02", "22:00")
    c.add_projection(2, "2D", "2014-04-02", "19:30")
    c.add_reservations("RadoRado", 1, 2, 1)
    c.add_reservations("RadoRado", 1, 3, 5)
    c.add_reservations("RadoRado", 1, 7, 5)
    c.add_reservations("Ivo", 3, 1, 1)
    c.add_reservations("Ivo", 3, 1, 2)
    c.add_reservations("Mysterious", 5, 2, 3)
    c.add_reservations("Mysterious", 5, 2, 4)
