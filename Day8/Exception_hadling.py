#================================ Exception =========================================
# Exception handling is used to handle runtime errors in a program so 
# that the program does not crash. It is done using try, except, else, and finally blocks.

#---------------------------------------------------------------------------------------------------

# Q1
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter first number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("cant divide by zero")
# except ValueError:
#     print("Enter only integer value :")
# except:
#     print("Some error occured")

#---------------------------------------------------------------------------------------------------
# Q2
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter only integer values")
# except Exception as msg:
#     print("Some error occurred:", msg)
# else:
#     print("Everything is OK")
# finally:
#     print("Program execution completed")

#---------------------------------------------------------------------------------------------------

# Q3
# Exception Handling with Logging in Python
# import logging
# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
# try:
#     a=int(input("enter"))
#     b=int(input("enter"))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("logging level is set up, check 'Newfile.txt) for log details")

#---------------------------------------------------------------------------------------------------

# Q4
# import csv
# f = open('employee.csv', 'a')
# a = csv.writer(f)
# # a.writerow(["EmpID","Emp Name","Emp Age"])
# # print('file has created')

# empid   = int(input("Enter your EmpID: "))
# empname = input("Enter Employee Name: ")
# age     = int(input("Enter Age"))
# a.writerow([empid,empname,age])
# print("file has created")

#---------------------------------------------------------------------------------------------------
#col name  studID, Studname, phy, chem, math, total, percentage,result
# 
# input = studided , student phy, chem, math
# calculate : total, percentage
#check condition all paper marks >= 40 pass else fail

# import csv
# # Open the file in append mode
# f = open("employee1.csv", "a", newline="")
# a = csv.writer(f)

# #a.writerow(["StudID","StudName","Physics","Chemistry","Maths", "Total", "Percentage", "Result"])

# # Get user inputs with correct labels
# StudID = int(input("Enter Student ID: "))
# StudName = input("Enter Student Name: ")
# Physics = int(input("Enter Physics marks: "))
# Chemistry = int(input("Enter Chemistry marks: "))
# Maths = int(input("Enter Maths marks: "))

# # Calculate total and percentage
# Total = Physics + Chemistry + Maths
# Percentage = round((Total / 300) * 100, 2)

# # Check pass/fail condition (all subjects must be >= 40)
# if Physics >= 40 and Chemistry >= 40 and Maths >= 40:
#     Result = "Pass"
# else:
#     Result = "Fail"

# # Write the data row to the CSV file
# a.writerow([StudID, StudName, Physics, Chemistry, Maths, Total, Percentage, Result])

# # Close the file connection
# f.close()

# print("Data successfully saved to file.")
