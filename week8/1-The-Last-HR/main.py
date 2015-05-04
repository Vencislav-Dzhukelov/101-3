import sqlite3


def main():
    db = sqlite3.connect('lastHR.db')
    cursor = db.cursor()
    exit = False
    while exit is False:
        command = input("Enter command from 1 to 3:").split(" ")
        if command[0] == "1":
            result = cursor.execute(
                "SELECT student_name, github_acc from Students")
            for row in result:
                print ("{0} - {1}".format(row[0], row[1]))
        elif command[0] == "2":
            result = cursor.execute("SELECT distinct course_name From Courses")
            for row in result:
                print (row[0])
        elif command[0] == "3":
            result = cursor.execute("SELECT student_name, course_name \
                                    From Students left join Student_to_Courses on Students.student_id = Student_to_Courses.student_id \
                                                    left join Courses on Student_to_Courses.course_id = Courses.course_id")
            for row in result:
                print ("{0} - {1}".format(row[0], row[1]))
        elif command[0] == "exit":
            exit = True
        else:
            print("Error! Invalid command!!!")

if __name__ == "__main__":
    main()
