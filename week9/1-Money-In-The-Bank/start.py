from sql_manager import Database
import getpass
import re
from Client import *
import hashlib




class Interface():
    def __init__(self, database):
        self._database = database

    def check_password(self, password):
            flag = True
            if len(password) < 8:
                flag = False

            if re.search('[a-z]', password) is None:
                flag = False
            if re.search('[A-Z]', password) is None:
                flag = False
            #if re.search('.,[,!,@,#,$,%,^,&,*,(,),_,~,-,]', password) is None:
             #   flag = False
            if re.search('[0-9]', password) is None:
                flag = False

            return flag


    def make_hash(self, password):
            hash_object = hashlib.sha1(password.encode("utf-8"))
            return hash_object.hexdigest()


    def main_menu(self):
        print("Welcome to our bank service. You are not logged in. \nPlease register or login")

        while True:
            command = input("$$$>")

            if command == 'register':
                username = input("Enter your username: ")
                email = input("Enter email:")
                password = getpass.getpass(prompt="Enter your password: ")

                if self.check_password(password) == True:
                    self._database.register(username, self.make_hash(password), email)
                    print("Registration Successfull")
                else:
                    print("Password is very week!Try again!")
                    continue

            elif command == 'login':
                username = input("Enter your username: ")
                password = getpass.getpass(prompt="Enter your password: ")

                logged_user = self._database.login(username, password)

                if logged_user:
                    self.logged_menu(logged_user)
                else:
                    print("Login failed")

            elif command == 'help':
                self._help()
            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def _help(self):
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

    def logged_menu(self, logged_user):
        print("Welcome you are logged in as: " + logged_user.get_username())
        while True:
            command = input("Logged>>")

            if command == 'info':
                print("You are: " + logged_user.get_username())
                print("Your id is: " + str(logged_user.get_id()))
                print("Your balance is:" + str(logged_user.get_balance()) + '$')

            elif command == 'changepass':
                new_pass = getpass.getpass(prompt="Enter your new password: ")
                self._database.change_pass(new_pass, logged_user)

            elif command == 'change-message':
                new_message = input("Enter your new message: ")
                self._database.change_message(new_message, logged_user)

            elif command == 'show-message':
                print(logged_user.get_message())

            elif command == 'help':
                print("info - for showing account info")
                print("changepass - for changing passowrd")
                print("change-message - for changing users message")
                print("show-message - for showing users message")


def main():
    database = Database()
    database.create_clients_table()

    interface = Interface(database)
    interface.main_menu()

if __name__ == '__main__':
    main()
