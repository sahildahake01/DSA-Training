# ========================================= CLASS in Python  =========================================

#  object is also called as reference variable
#---------------------------------------------------------------------------------------------------

#Q1
# class Name:
#     age = 30 #data member
#     def display(self): #method
#         print('hello world')

# obj = Name()
# print(obj.age)
# obj.display()
#---------------------------------------------------------------------------------------------------

#Q2
# class Student:
#     def __init__(self):
#         self.name ="Sahil"
#         self.age = 23
    
#     def display(self):
#         print("Name: ", self.name)
#         print("age: ", self.age)

# StudObj = Student()
# print(StudObj) #op = <__main__.Student object at 0x000002B779B67230>

#---------------------------------------------------------------------------------------------------

#Q3
# class Message:
#     def __init__(self):
#         print("i am a constructor")
    
#     def shows(self):
#         print("class program")

# obj = Message() # op --> i am a constructor
# obj.shows() #class program
# obj2 = Message()   #for each obj, constructor is called once..

#---------------------------------------------------------------------------------------------------

#Q4
# class StudentInfo:
#     def __init__(self,name,age,roll_no):
#         self.Name= name
#         self.Age= age
#         self.Roll_no= roll_no

#     def displayStudentInfo(self):
#         print("Name: ",self.Name)
#         print("Age: ",self.Age)
#         print("Roll_no: ",self.Roll_no)

# studobj = StudentInfo("sahil",32,101)
# studobj.displayStudentInfo()
#---------------------------------------------------------------------------------------------------
