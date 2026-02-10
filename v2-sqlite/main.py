from database import create_table
create_table()
import os
import manager
obj = manager.StudentManager()
while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. List All Students")
    print("6. Exit")
    try:
        user_input = int(input("Select which option : "))
        # add student
        if(user_input == 1):
            obj.add_student()
        # view student
        elif(user_input == 2):
            user_id = int(input("Enter which student id to view : "))
            obj.view_student(user_id)
        # update student
        elif(user_input == 3):
            user_id = int(input("Enter which student id to update : "))
            obj.update_student(user_id)
        # delete student
        elif(user_input == 4):
            user_id = int(input("Enter which student id to delete : "))
            obj.delete_student(user_id)
        # list students
        elif(user_input == 5):
            obj.list_students()
        # exit
        elif(user_input == 6):
            print("Exiting program")
            break
        else:
            print("------- Enter correct option -------")
    except ValueError:
        print("------- Enter a valid number -------")
# To clear previous terminal data
os.system('cls' if os.name == 'nt' else 'clear')

# Search by name/email feature (string filtering).
# Sort by grade or age dynamically.
# Export student list to CSV file (practice CSV module).