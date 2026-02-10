import json
class StudentManager:
    def load_students(self):
        try:
            with open('students.json','r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self, data):
        with open('students.json','w') as file:
            json.dump(sorted(data, key=lambda item: item['id']), file, indent=4)

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Enter a valid number")

    def add_student(self):
        from student import StudentDetails
        id = self.get_int_input("id : ")
        name = input("name : ")
        age = self.get_int_input("age : ")
        grade = input("grade : ")
        email = input("email : ")
        stdobj = StudentDetails(id, name, age, grade, email)
        data = self.load_students()
        data.append(stdobj.to_dict())
        self.save_students(data)
        print("Added")

    def view_student(self, id):
        data = self.load_students()
        if not data:
            print("No data found")
            return
        for user in data:
            if(user['id'] == id):
                print(f"ID: {user['id']} | Name: {user['name']} | Age: {user['age']} | Grade: {user['grade']} | Email: {user['email']}")
                return
        print(f"Student with ID {id} not found.")

    def delete_student(self, id):
        data = self.load_students()
        if not data:
            print("No data found")
        found = False
        for user in data:
            if(user['id'] == id):
                data.remove(user)
                found = True
        # --- keep only those whose id does not match (best for larger data) ---
        # new_data = [user for user in data if user['id'] != id]
        # if len(new_data) == len(data):
        #     print(f"Student with ID {id} not found")
        #     return
        # self.save_students(new_data)
        # print("Deleted")
        if found:
            self.save_students(data)
            print("Deleted")
        else:
            print(f"Student with ID {id} not found")

    def list_students(self):
        data = self.load_students()
        # For readable in terminale
        print("------- Student List -------")
        if not data:
            print("No students found")
        for student in data:
            print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | Email: {student['email']}")
        print("----------------------------")
        
    def update_student(self, id):
        data = self.load_students()
        if not data:
            print("No data found")
        found = False
        for user in data:
            if(user['id'] == id):
                print("Enter new updating details")
                new_id = self.get_int_input("id : ")
                new_name = input("name : ")
                new_age = self.get_int_input("age : ")
                new_grade = input("grade : ")
                new_email = input("email : ")
                if new_id: user['id'] = int(new_id)
                if new_name: user['name'] = str(new_name)
                if new_age: user['age'] = int(new_age)
                if new_grade: user['grade'] = str(new_grade)
                if new_email: user['email'] = str(new_email)
                found = True
        if found:
            self.save_students(data)
            print("Updated")
        else:
            print(f"Student with ID {id} not found.")