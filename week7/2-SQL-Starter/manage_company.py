import sqlite3


def list_employees():
    db = sqlite3.connect('company.db')
    cursor = db.cursor()
    result = cursor.execute("SELECT id, name, position from company")
    for row in result:
        print ("{0} - {1} - {2}".format(row[0], row[1], row[2]))


def monthly_spending():
    db = sqlite3.connect('company.db')
    cursor = db.cursor()
    cursor.execute("SELECT sum(monthly_salary) FROM company")
    result = cursor.fetchone()
    return ("The company is spending ${0} every month!".format(result[0]))


def yearly_spending():
    db = sqlite3.connect('company.db')
    cursor = db.cursor()
    cursor.execute("SELECT sum(monthly_salary)*12 + sum(yearly_bonus) FROM company")
    result = cursor.fetchone()
    return ("The company is spending ${0} every year!".format(result[0]))


def input_data():
    name = input("Employee Name: ")
    salary = input("Monthly Salary: ")
    bonus = input("Yearly Bonus: ")
    position = input("Position: ")
    return (name, salary, bonus, position)

def add_employee():
    db = sqlite3.connect('company.db')
    cursor = db.cursor()
    new_info = input_data()
    cursor.execute("INSERT into company(name, monthly_salary, yearly_bonus, position) \
                values (?, ?, ?, ?)", (new_info[0], new_info[1], new_info[2], new_info[3]))
    db.commit()


def delete_employee(id):
    db = sqlite3.connect('company.db')
    cursor = db.cursor()
    cursor.execute("DELETE FROM company WHERE id = ?", (id,))
    db.commit()
    print ("Delete completed")


def update_employee(id):
    db = sqlite3.connect('company.db')
    cursor = db.cursor()
    update_info = input_data()
    cursor.execute("""UPDATE company SET name = ?, monthly_salary = ?,
        yearly_bonus = ?, position = ? WHERE id = ?""",
                   (update_info[0], update_info[1], update_info[2], update_info[3], id))
    db.commit()


def main():
    exit = False
    while exit is False:
        command = input("Enter command:").split(" ")
        if command[0] == "list_employees":
            list_employees()
        elif command[0] == "monthly_spending":
            print(monthly_spending())
        elif command[0] == "yearly_spending":
            print(yearly_spending())
        elif command[0] == "add_employee":
            add_employee()
        elif command[0] == "delete_employee":
            delete_employee(command[1])
        elif command[0] == "update_employee":
            update_employee(command[1])
        elif command[0] == "exit":
            exit = True
        else:
            print("Error! Invalid command!!!")



if __name__ == "__main__":
    main()
    # list_employees()
    # print (monthly_spending())
    # print (yearly_spending())
    # add_employee()
    # delete_employee(6)
