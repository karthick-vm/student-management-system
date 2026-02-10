import sqlite3
from database import get_connection
class StudentManager:
    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Enter a valid number")

    def add_student(self):
        conn = get_connection()
        cursor = conn.cursor()
        print("Enter student details \n")
        id = self.get_int_input("id : ")
        name = input("name : ")
        age = self.get_int_input("age : ")
        grade = input("grade : ")
        email = input("email : ")
        try:
            cursor.execute(
                "INSERT INTO students (id, name, age, grade, email) VALUES (?, ?, ?, ?, ?)",
                (id, name, age, grade, email,) # (?) - parameterized query - prevents sql ingection
            )
            conn.commit()
            print("Added")
        except sqlite3.IntegrityError: 
            print("Student ID already exists")
        conn.close()

    def view_student(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM students WHERE id = ?", (id,)
        )
        #fetchone,fetchmany(size),fetchall- this all convert to tuple so in (id,) used (,) for tuple
        student = cursor.fetchone() 
        if student:
            print(student)
        else:
            print(f"Student with ID {id} not found")
        conn.close()

    def delete_student(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM students WHERE id = ?", (id,)
        )
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Student with ID {id} not found")
        else:
            print("Deleted")
        conn.close()

    def list_students(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM students ORDER BY id"
        )
        students = cursor.fetchall()
        if students:
            for student in students:
                print(student)
        else:
            print("No students found")
        conn.close()

    def update_student(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        print("Enter new student details \n")
        name = input("New name: ")
        age = self.get_int_input("New age: ")
        grade = input("New grade: ")
        email = input("New email: ")
        cursor.execute(
            """UPDATE students
                    SET name = ?, age = ?, grade = ?, email = ?
                    WHERE id = ?
            """, (name, age, grade, email, id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            print(f"Student with ID {id} not found")
        else:
            print("Updated")
        conn.close()