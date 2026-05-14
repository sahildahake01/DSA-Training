# def hello(): #called function
#     print("hakuna matata")

# hello() # calling function
# hello()
#-----------------------------------------------------------------------------------------------------------------------

# def arithmatic():
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     sum= a+b
#     sub= a-b
#     div= a/b
#     mul= a*b
#     return sum, sub, div, mul

# print(arithmatic())

#-----------------------------------------------------------------------------------------------------------------------

# def arithmatic():
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     sum= a+b
#     sub= a-b
#     div= a/b
#     mul= a*b
#     return sum, sub, div, mul

# result =arithmatic()
# print('Arithmatic',result)

#-----------------------------------------------------------------------------------------------------------------------

# def arithmatic(a,b):
#     sum= a+b
#     sub= a-b
#     div= a/b
#     mul= a*b
#     return sum, sub, div, mul

# result = arithmatic(5,5)
# print("arithmatic: ",result)    #op is arithmatic:  (10, 0, 1.0, 25)

#-----------------------------------------------------------------------------------------------------------------------

# def credential(username,password):
#     if username == password:
#         print("login successfully..")
#     else:
#         print("invalid credential")

# credential(username="sahil",password="sahil")  #op is login successfully..

#-----------------------------------------------------------------------------------------------------------------------

# def cityname(city="pune"):
#     print(city)

# cityname("Nagpur") #Nagpur
# cityname("mumbai") #mumbai
# cityname() #pune

#-----------------------------------------------------------------------------------------------------------------------

# def cityname(*city): # *city - accept multiple values
#     print(city)

# cityname("nagpur","bhandara","nashik","rahuri") #op  ('nagpur', 'bhandara', 'nashik', 'rahuri')

#-----------------------------------------------------------------------------------------------------------------------

#MODULARITY APPROACH IN FUNCTIONS
#-----------------------------------------------------------------------------------------------------------------------

# import sys
# def add():
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     print('addition: ',a+b)
# def sub():
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     print('subtraction: ',a-b)

# def div():
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     print('divisions: ',a/b)

# def mul():
#     a = int(input("enter value of a: "))
#     b = int(input("enter value of b: "))
#     print('multiplication: ',a*b)

# while True:
#     print("----------------------------")
#     print("1. ADDITION")
#     print("2. SUBTRACTION")
#     print("3. DIVISION")
#     print("4. MULTIPLICATION")
#     print("5. EXIT")
#     Choice = int(input("Enter your choice [1-5]: "))
#     if Choice == 1:
#         add()
#     elif Choice == 2:
#         sub()
#     elif Choice == 3:
#         div()
#     elif Choice == 4:
#         mul()
#     elif Choice == 5:
#         sys.exit()

#-----------------------------------------------------------------------------------------------------------------------
# i = 1             #simple while loop example
# while i<=5:
#     print(i)
#     i+=1=
# 1 2 3 4 5

#-----------------------------------------------------------------------------------------------------------------------