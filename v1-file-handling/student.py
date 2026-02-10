class StudentDetails:
    def __init__(self, id, name, age, grade, email):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email
    
    def to_dict(self):
        return {"id": self.id, "name": self.name, "age": self.age, "grade": self.grade, "email": self.email}
    
# stdobj = student(id, name, age, grade, mail)