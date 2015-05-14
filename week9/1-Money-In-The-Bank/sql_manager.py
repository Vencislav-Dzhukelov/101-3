import sqlite3
from Client import Client


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("bank.db")
        self.cursor = self.conn.cursor()

    def create_clients_table(self):
        create_query = '''create table if not exists
            clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    email TEXT,
                    password TEXT,
                    balance REAL DEFAULT 0,
                    message TEXT)'''

        self.cursor.execute(create_query)

    def change_message(self, new_message, logged_user):
        self.cursor.execute("UPDATE clients \
                            SET message = ? \
                            WHERE id = ?", (new_message, logged_user.get_id()))
        self.conn.commit()
        logged_user.set_message(new_message)

    def change_pass(self, new_pass, logged_user):
        self.cursor.execute("UPDATE clients\
                        SET password = ?\
                        WHERE id = ?", (new_pass, logged_user.get_id()))
        self.conn.commit()

    def register(self, username, password, email):
        insert_sql = "insert into clients (username, password, email) values (?, ?, ?)"
        self.cursor.execute(insert_sql, (username, password, email))
        self.conn.commit()

    def login(self, username, password):
        select_query = "SELECT id, username, balance, message, email\
                        FROM clients\
                        WHERE username = ? AND password = ? LIMIT 1"

        self.cursor.execute(select_query, (username, password))
        user = self.cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3], user[4])
        else:
            return False
