import string
import random
from pathlib import Path
import json


class Students:
    data = []
    count = 0 
    database = "students.json"

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
                print(data)
    except Exception as err:
        print(err)

    @classmethod
    def randomid(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        dig = random.choices(string.digits,k= 3)
        sym =random.choices("!@#$%^&*",k=2)
        q = alpha + dig + sym
        random.shuffle(q)
        return "".join(q)
    
    @classmethod
    def updateInfo(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))


    def regestration(self):
        stu = {
            "id" : Students.randomid(),
            "name" : input("Enter name"),
            "email" : input("enter email"),
            "password" : input("enter password"), 
            "skill" : input("enter skill")
        }
        Students.data.append(stu)
        Students.updateInfo()
    
    def readAllStudents(self):
        counter = 1
        for i in Students.data:
            print()
            print(counter)
            print()
            for j in i.keys():
                print(f"{j} -> {i[j]}")
            counter+=1
    

    @classmethod
    def readSingleStudent(cls):
        student_id = input("Enter student ID to read details: ")
        found = False
        for student in cls.data:
            if student["id"] == student_id:
                found = True
                print("Student Details:")
                for key, value in student.items():
                    print(f"{key}: {value}")
                break
        if not found:
            print("Student not found.")

    @classmethod
    def editStudent(cls):
        student_id = input("Enter student ID to edit details: ")
        found = False
        for student in cls.data:
            if student["id"] == student_id:
                found = True
                print("Editing student details:")
                for key in student.keys():
                    new_value = input(f"Enter new {key} (leave empty to keep current value): ")
                    if new_value:
                        student[key] = new_value
                cls.updateInfo()
                print("Student details updated successfully.")
                break
        if not found:
            print("Student not found.")

    @classmethod
    def deleteStudent(cls):
        student_id = input("Enter student ID to delete: ")
        found = False
        for student in cls.data:
            if student["id"] == student_id:
                found = True
                cls.data.remove(student)
                cls.updateInfo()
                print("Student deleted successfully.")
                break
        if not found:
            print("Student not found.")

student = Students()

print("press 1 for registration")
print("press 2 for details")
print("press 3 to read single student")
print("press 4 to edit details")
print("press 5 to delete a user")
print("press 6 to exit")

n = input("please tell what you want to do")

if n == "1":
    student.regestration()
if n == "2":
    student.readAllStudents()
if n == "3":
    student.readSingleStudent()
if n == "4":
    student.editStudent()
if n == "5":
    student.deleteStudent()
if n == "6":
    print("Exiting the program.")
    exit()