
#Q1
# salary = int(input('Enter your salary: '))
# rating = float(input('Enter your performance appraisal rating: '))
# increament = 0
# if rating >=1 and rating<=3:
#     increament = salary*10/100
# elif rating>=3.1 and rating<=4:
#     increament = salary*30/100
# elif rating>=4.1 and rating<=5:
#     increament = salary*40/100
# else:
#     print('Invalid rating')
# print('Incremented Salary: ' ,increament+salary)

#-----------------------------------------------------------------------------------------------------------------------

#Q2
# salary = 20000
# HRA = salary*20/100
# TA = salary*30/100
# DA = salary*45/100
# total_allowances = HRA + TA +DA
# print('Basic Salary: ',salary)
# print('HRA:',HRA,'','TA:',TA,'','DA:',DA)
# print("GROSS SALARY", salary + total_allowances)

#-----------------------------------------------------------------------------------------------------------------------
#student module
# class Student:
#     def __init__(self, sid, roll, name, city):
#         self.sid = sid
#         self.roll = roll
#         self.name = name
#         self.city = city


# class StudentManagementSystem:
#     def __init__(self):
#         self.students = []

#     # Add Student
#     def add_student(self):
#         sid = int(input("Enter Student ID: "))
#         roll = int(input("Enter Student Roll No: "))
#         name = input("Enter Student Name: ")
#         city = input("Enter Student City: ")

#         s = Student(sid, roll, name, city)
#         self.students.append(s)

#         print("\nStudent Added Successfully\n")

#     # Show Student
#     def show_student(self):
#         if len(self.students) == 0:
#             print("\nNo Student Record Found\n")

#         else:
#             print("\nStudent Records\n")

#             print("ID\tROLL\tNAME\t\tCITY")

#             for s in self.students:
#                 print(f"{s.sid}\t{s.roll}\t{s.name}\t{s.city}")

#             print()

#     # Update Student
#     def update_student(self):
#         sid = int(input("Enter Student ID: "))

#         found = False

#         for s in self.students:

#             if s.sid == sid:
#                 found = True

#                 print("\nMatched Student Data Are:\n")

#                 print("1. Student Roll No:", s.roll)
#                 print("2. Student Name:", s.name)
#                 print("3. Student City:", s.city)
#                 print("4. Don't Want to Update")

#                 choice = int(input("\nSelect Above Option: "))

#                 if choice == 1:
#                     new_roll = int(input("Enter New Roll No: "))
#                     s.roll = new_roll
#                     print("\nRoll No Updated Successfully\n")

#                 elif choice == 2:
#                     new_name = input("Enter New Name: ")
#                     s.name = new_name
#                     print("\nName Updated Successfully\n")

#                 elif choice == 3:
#                     new_city = input("Enter New City: ")
#                     s.city = new_city
#                     print("\nCity Updated Successfully\n")

#                 elif choice == 4:
#                     print("\nUpdate Cancelled\n")

#                 else:
#                     print("\nInvalid Choice\n")

#         if found == False:
#             print("\nStudent Not Found\n")

#     # Delete Student
#     def delete_student(self):
#         sid = int(input("Enter Student ID: "))

#         found = False

#         for s in self.students:

#             if s.sid == sid:
#                 self.students.remove(s)
#                 found = True
#                 print("\nStudent Deleted Successfully\n")
#                 break

#         if found == False:
#             print("\nStudent Not Found\n")


# # Main Program
# sms = StudentManagementSystem()

# while True:

#     print("===== Student Management System =====")
#     print("1. Add Student")
#     print("2. Show Student")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Exit")

#     choice = int(input("Select Any Choice: "))

#     if choice == 1:
#         sms.add_student()

#     elif choice == 2:
#         sms.show_student()

#     elif choice == 3:
#         sms.update_student()

#     elif choice == 4:
#         sms.delete_student()

#     elif choice == 5:
#         print("\nThank You")
#         break

#     else:
#         print("\nInvalid Choice\n")
