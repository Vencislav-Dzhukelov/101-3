import sqlite3
from download_students import StudentData


class Create():
    def make_db(self):
        db = sqlite3.connect('lastHR.db')
        cursor = db.cursor()
        create_table_students = """
        CREATE TABLE IF NOT EXISTS Students( student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            student_name TEXT, github_acc TEXT)
        """
        cursor.execute(create_table_students)

        create_table_courses = """
        CREATE TABLE IF NOT EXISTS Courses( course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            course_name TEXT)
        """
        cursor.execute(create_table_courses)

        create_table_students_to_courses = """
        CREATE TABLE IF NOT EXISTS Student_To_Courses(st_to_co_id INTEGER PRIMARY KEY,
                                    student_id INTEGER ,
                                    course_id INTEGER,
                                    group_number INTEGER,
                                    FOREIGN KEY(student_id) REFERENCES Students(student_id),
                                    FOREIGN KEY(course_id) REFERENCES Courses(course_id))
        """
        cursor.execute(create_table_students_to_courses)

    def add_info(self, data):
        db = sqlite3.connect('lastHR.db')
        cursor = db.cursor()
        for items in data:
            cursor.execute("INSERT into Students(student_name, github_acc) \
                            values(?, ?)", (items["name"], items["github"]))

            last_student_id = cursor.lastrowid
            cursor.execute("INSERT into Student_To_Courses(student_id) \
                            values(?)", (last_student_id,))

            for items2 in items["courses"]:
                cursor.execute("INSERT into Courses(course_name) \
                                values(?)", (items2["name"],))

                last_course_id = cursor.lastrowid
                cursor.execute("UPDATE Student_To_Courses \
                                SET course_id = ? \
                                Where student_id = ?", (last_course_id,last_student_id))
                cursor.execute("UPDATE Student_To_Courses \
                                SET group_number = ? \
                                Where student_id = ?", (items2["group"],last_student_id))
        db.commit()


c = Create()
d = StudentData()
if __name__ == "__main__":
    # c.make_db()
    # c.add_info(d.get_data())
