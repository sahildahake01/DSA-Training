#Q1
# def func(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0]) #3 44
#------------------------------------------------------------------------------------------

#Q2
# def f(i,values =[]):
#     values.append(i)
#     print(values)

# f(1)    #[1]
# f(2)    #[1, 2]
# f(3)    #[1, 2, 3]
#------------------------------------------------------------------------------------------

#Q3
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] =1

# addone('Apple')
# addone('banana')
# addone('apple')
# print(len(fruit))  #3

#----------------------------------------------------------------------------------------------------------------------

#Q4
# write a program to accept name and marks from the Keyboard
# and creates a dictionary also display marks by taking student name

# n = int(input("enter no. of students: "))
# d = {}
# for i in range(n):
#     name = input('enter Student Name: ')
#     marks = input('Enter student marks: ')
#     d[name]=marks
# while True:
#     name=input('Enter Student Name to get Marks: ')
#     marks=d.get(name,-1)
#     if marks == -1:
#         print('Student not found')
#     else:
#         print('The Marks of ',name,'are',marks)
#     option = input('Do you want to find another student marks[YES|NO]: ')
#     if option=='no':
#         break
# print('Thanks for using our application')

#-----------------------------------------------------------------------------------------------------------------------

#Q5
# write a program to access each character of string in forward and backward direction by using while loop
#i/p = 'Learning Python is very easy'
# s= 'Learning Python is very easy'
# n=len(s)
# i=0
# print("forward")
# while i<n:
#     print(s[i],end='')
#     i +=1
# print()
# print('Backward')
# i=-1
# while i>= -n:
#     print(s[i],end='')
#     i=i-1

#-----------------------------------------------------------------------------------------------------------------------

#Q6
# # check for blank and print previous value
# s = input() #abcdfjgerj abcdfijger
# for i in range(1,len(s)):
#     if s[i] == ' ':
#         print(s[i-1]) #j

#-----------------------------------------------------------------------------------------------------------------------

#Q7
# v=['a','e','i','o','u']
# w=input('enter word where we will search the vowels: ')         #sahilisgoodboy 
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('found vowels: ',found)                                   #found vowels:  ['a', 'i', 'o']
# print('unique vowels ',len(found),  'from the given word= ',w)  #unique vowels  3 from the given word=  sahilisgoodboy

#-----------------------------------------------------------------------------------------------------------------------

#Q8
# x,y,z = map(int, input().split())
# mylist =[]
# for i in range(x):
#     a= int(input())
#     mylist.append(a)

# for j in mylist:
#     if j>=y and j<=z:
#         print(j ,end=' ')

#-----------------------------------------------------------------------------------------------------------------------

#Q9
# import datetime
# date=datetime.datetime.now()
# print("It's now: {:%d/%m/%Y %H:%M:%S}".format(date) )     #It's now: 16/05/2026 14:49:44

#-----------------------------------------------------------------------------------------------------------------------

#Q10
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)   #True
# print(x==z)   #false
# print(x!=z)   #true

#-----------------------------------------------------------------------------------------------------------------------

#Q11        LIST COMPRESSION
# val=[2**i for i in range(1,6)]    # logic | loop and range
# print(val)                        #[2, 4, 8, 16, 32]

#-----------------------------------------------------------------------------------------------------------------------

#Q12
# s=[i*i for i in range(1,11)]      # logic | loop and range
# print(s)                          #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#-----------------------------------------------------------------------------------------------------------------------

#Q13        DICTIONARY COMPRESSION
# sqr={x:x*x for x in range(1,6)}
# print(sqr)                          #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#-----------------------------------------------------------------------------------------------------------------------

#Q14
# doubles={x:2*x for x in range(1,6)}
# print(doubles)                      #{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

#-----------------------------------------------------------------------------------------------------------------------

#Q15
#how to read multiple values from keyboard in a string
# a,b=[int(x) for x in input("Enter 2 numbers: ").split()]    #Enter 2 numbers: 22 43
# print("product is ",a*b)                                    #product is  946

#-----------------------------------------------------------------------------------------------------------------------

#Q16
# a,b,c = [float(x) for x in input("Enter 3 float numbers: ").split()]    #Enter 3 float numbers: 4.5 3.1 6.3
# print("The sum is ",a+b+c)                                              #The sum is  13.899999999999999

#-----------------------------------------------------------------------------------------------------------------------

#Q17
#using else block in for loop
# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print(item," => This is not in your budget..!")
#         continue
#     print(item)
# else:
#     print('you have purchased everything')

#-----------------------------------------------------------------------------------------------------------------------

#Q18
#validate username and password
# while True:
#     u= input('Username: ')
#     p= input('Password: ')
#     if u=='admin' and p=='admin':
#         print('login successfull..')
#         break
#     else:
#         print('--Reenter username and password--')


#-----------------------------------------------------------------------------------------------------------------------

#Q19
#tower of honai
import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HONAI GAME")
        print()
        print("Given Problem:       A=[3,2,1]    B=[]   c[] ")
        print()
        print('Expected Output:     A=[]         B=[]   c[3,2,1]')
        print()
        self.A =[]
        self.B =[]
        self.C =[]
    
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A= ",self.A)
        print("items in tower A\n")
    
    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(1)
        print('A= ',self.A  ,"      ",'B= ',self.B  ,"      "'C= ',self.C)
        print("=============Pass ONE completed=============\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(1)
        print('A= ',self.A  ,"      ",'B= ',self.B  ,"      "'C= ',self.C)
        print("=============Pass TWO completed=============\n")

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(1)
        print('A= ',self.A  ,"      ",'B= ',self.B  ,"      "'C= ',self.C)
        print("=============Pass THREE completed=============\n")
    
    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print('A= ',self.A  ,"      ",'B= ',self.B  ,"      "'C= ',self.C)
        print("=============Pass FOUR completed=============\n")

    def pass5(self):
        self.temp = self.B.pop(0)
        self.A.append(self.temp)
        time.sleep(1)
        print('A= ',self.A  ,"      ",'B= ',self.B  ,"      "'C= ',self.C)
        print("=============Pass FIVE completed=============\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print('A= ',self.A  ,"      ",'B= ',self.B  ,"      "'C= ',self.C)
        print("=============Pass SIX completed=============\n")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(1)
        print('A= ',self.A  ,"      ",'B= ',self.B  ,"      "'C= ',self.C)
        print("=============Pass SEVEN completed=============\n")

obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
print("problem solved")