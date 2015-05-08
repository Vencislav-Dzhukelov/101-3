import sqlite3
db = sqlite3.connect("movie_database.db")
cursor = db.cursor()


def show_movies():
    list_of_movies = cursor.execute(
        '''SELECT id, name, rating FROM Movies ORDER BY rating desc''')
    for item in list_of_movies:
        print("[{}] - {} - {}".format(item[0], item[1], item[2]))


def show_projections(movie_id, date=None):
    if date is None:
        result = cursor.execute("SELECT * FROM Projections\
                                WHERE movie_id = ?\
                                order by date asc, time asc", (movie_id, ))

        for item in result:
            print("[{}] - {} {} {}".format(item[0], item[3], item[4], item[2]))
    else:
        result = cursor.execute("SELECT * FROM Projections\
                                WHERE movie_id = ? and date = ?\
                                order by date asc, time asc", (movie_id, date))

        for item in result:
            print("[{}] - {} {} {}".format(item[0], item[3], item[4], item[2]))


if __name__ == "__main__":
    show_movies()
    show_projections(1)
    show_projections(1, "2014-04-01")
