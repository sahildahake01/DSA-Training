#why python is called as dynamically typed language?
# age = 39
# pi = 3,14
# name = "sahil"
# result = True
# print(type(age))
# print(type(pi))
# print(type(name))
# print(type(result))

# print(id(age))
# print(id(pi))
# print(id(name))
# print(id(result))

#why all fundamental datatypes are imutable?
# math = 50
# chem = 50
# phys = 50
# print(id(math))
# print(id(chem))
# print(id(phys))
#All id's will be same 140721192438216

# print(2+2)
# print("2"+"2")

# a = int(input("enter first num:  "))
# b = int(input("enter second num: "))
# print(a+b)
#input fuction by defalt taking as string 

#typecasting------------------------------------------------------------------------------
# print(int(3.14))  #3
# # print(int(10+5j))
# print(int(True))  #1
# print(int(False))  #0
# # print(int(4.22))
# print(int("4"))  #4
# # print(int("sahil"))

# #complex() used to convert
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# print(complex(5,-3))
# print(complex(True,False))

# #bool() is used to convert
# print(bool(0)) #false
# print(bool(15)) #true
# print(bool(3.14)) #true
# print(bool(0.0)) #false
# print(bool(1+2j)) #true
# print(bool(0+0j)) #false
# print(bool(-1)) #true
# print(bool(False)) #false
# print(bool(True)) #true
# print(bool("")) #false
# -----------------------------------------------------------------------------------------

# #simple if
# a = int(input("enter any single digit: "))
# if a >0:
#     print("positive number")
# if a<0:
#     print("negative number")
# if a ==0:
#     print("zero")

# #if-else
# day = input("Enter your day: ")

# if day == "saturday" or day == "sunday" or day == "SATURDAY" or day == "SUNDAY":
#     print("weekend")
# else:
#     print("working day")

# #elif
# per = 65
# if per >=65:
#     print("Grade=A")
# elif per <=65 and per >=50:
#     print("Grade=B")
# else:
#     print("Fail")

# chr = ord(input("enter any one character: "))# ord is used convert to asscii value
# if chr >=65 and chr<90:
#     print("Upper case")
# elif chr >97 and chr <=122:
#     print("lower case")
# elif chr >48 and chr <=57:
#     print("digit")
# else:
#     print("special character")
#-------------------------------------------------------------------------------------------------

# name = "help4code"
# print('h' not in name) # false
# print('a' not in name) #true

#identity operator (address comparison)
# math = 50
# chem = 50
# print(math is chem)
#-------------------------------------------------------------------------------------------------

# for i in range(5):
#     print(i)
# for i in range(2,11,2): ##range(start,end-1,increment by 2)
#     print(i)
# for i in range(5,0,-1):  #range(start,end-1,decrement by 1)
#     print(i)
# for i in range(1,11):
#     print(i*2)

#we need to make table like this  1 2 3 4 5 6 7 8 9 10 in table form

# for i in range(1,11):
#     print(i*2, "    ", i*3, "   ", i*4, "  ", i*5, " ", i*6, "    ", i*7, "   ", i*8, "  ", i*9, " ", i*10)

# print("_____________________________________________________________________")

# for i in range(1,11):
#     print(i*11, "   ", i*12,"   " , i*13,"   " , i*14,"   " , i*15,"   " , i*16,"   " , i*17,"   " , i*18,"   " , i*19,"   " , i*20)

#--------------------------------------------------------------------------------------------------------------------------

# write a program to accept their pepar marks and
# calcute total, precentage, and check if he/she is passed in all the subject 
# so pass else print fail
# if percentage is greater than 65 and gender ="male" so he is eligible for placement else not eligible

# math = int(input("enter maths marks: "))
# chem = int(input("enter chem marks: "))
# phys = int(input("enter phys marks: "))
# gender = input("Enter your gender (M/F): ")

# total = math + chem + phys
# per = total/3
# print("Total Marks:",total)
# print("Percentage: ",per)
# if math >=35 and chem >=35 and phys >=35:
#     print("congrats! you're passed")
# else:
#     print("you are failed")

# if per >=65 and gender =="M":
#     print("You're eligible for placement!")
# else:
#     print("You're Not eligible for placement!")
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# print output given below
# 1   5     first iteration
# 2   4     second iteration
# 4   2     third iteration
# 5   3     fourth iteration
# for i in range(1,6):
#     print(i,"   ",6-i)
# print()
# #another method using zip() can include multiple range()
# for i,j in zip(range(1,6), range(5,0,-1)):
#     print(i,"   ",j)s

#-----------------------------------------------------------------------------------------------------------------------------------------------
#collections in python
#-----------------------------------------------------------------------------------------------------------------------------------------------

# mylist = ["prashant", "Ashish", "komal", "Ankush", "Ash", 77, "Sandip", 68.52, "Sahil"]
# print(mylist)
# print(type(mylist))
# print(mylist[0]) #prashant
# print(mylist[1]) #Ashish
# print(mylist[2]) #komal
# print(mylist[-1]) #Sahil
# print(mylist[2:5]) #komal, Ankush, Ashish
# print(mylist[:5]) #prashant, Ashish, komal, Ankush, Ashish
# print(mylist[1:]) #Ashish, komal, Ankush, Ashish, 77, Sandip, 68.52, Sahil
# print(mylist[::2]) #prashant, komal, Ashish, Sandip, Sahil

# mylist[2]= "komal patil"
# print(mylist)

# if "Ankush" in mylist:
#     print("Ankush is available")
# else:   
#     print("Not  Available")

# mylist.append("harsh")  #always add element at the end of the list
# mylist.append("laxman")
# print(mylist)

# mylist.insert(3,"Sanket") #insert element at specific index
# print(mylist)

# mylist.remove("Sandip") #remove first occurrence of element
# print(mylist)

# newlist = mylist.copy() #clone
# print(newlist)

# mylist = [['prashant', 'Jha'], ['85.56'], [440022,"yyy"]]
# print("Example of multidimensional list: ")
# print(mylist)
# print(mylist[0][0]) #prashant
# print(mylist[0][1]) #Jha
# print(mylist[1][0]) #85.56
# print(mylist[2][0]) #440022
# print(mylist[2][1]) #yyy

# list2 = [50,25,50,'prashant']
# del list2[0] #delete element at index 0
# print(list2) # [25, 50, 'prashant'] 
# del list2
# print(list2) #name error because list2 is deleted from memory

# list2 = [50,25,50,'prashant']
# list2.clear() #clear all elements from list but list will be exist in memory
# print(list2) # [] empty list

# name="Prashant"
# print(name)
# myname=list(name)
# print(myname) #['P', 'r', 'a', 's', 'h', 'a', 'n', 't']

# mylist = [44, 22, 77, 0, 9, 88]
# mylist.sort() #sort in ascending order
# print(mylist) #[0, 9, 22, 44, 77, 88]

# mylist =[44, 22, 77, 0, 9, 88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# mylist =[44, 22, 77, 0, 9, 88]
# for i in mylist:
#     print(i)
#----------------------------------------------------------------------------------------------------

#i/p =[0,1,4,0,2,5]
#o/p =[1,4,2,5,0,0]
# mylist = [0,1,4,0,2,5]
# for i in mylist:
#     if i ==0:
#         mylist.remove(i)
#         mylist.append(i)
# print(mylist)
#-----------------------------------------------------------------------------------------

#Q1
#find the second largest element
# list1 = [7,3,9,2,8]
# list1.sort()
# print("Second Largest:",list1[-2])
#------------------------------------------------------------------------------------------

#Q2
#[::2] :start   :end    2 increment
# a = [1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a) #error: attempt to assign sequence of size 6 to extended slice of size 5
#------------------------------------------------------------------------------------------

#Q3
# a=[1,2,3,4,5]
# print(a[3:0:-1]) #3 start, 0 stop, index 3 --> value 4 , flow 3 > 2 > 1 , o/p = 4,3,2
#------------------------------------------------------------------------------------------

#Q4
# arr = [[1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]]
# for i in range(0,4): #only focused on your row's
#     print(arr[i].pop())   #o/p= 4 7 11 15
#------------------------------------------------------------------------------------------

#Q5
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i - 1] = arr[i]
# for i in range(0,6):
#     print(arr[i], end = " ")
#------------------------------------------------------------------------------------------

#Q6
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]#  : it selects all elements in fruit_list1
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kivi'

# sum=0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum+=1
#     if ls[1] == 'Kivi':
#         sum+=20
# print(sum) #22
#-------------------------------------------------------------------------------------------

#Q7 find common elements in three lists
# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)
#------------------------------------------------------------------------------------------

#Q8 find the sum of all elements in the list
# mylist =[]
# N= int(input("enter the value of N: "))
# for i in range(N):
#     val = int(input("enter the elements: "))
#     mylist.append(val)
# # print(len(mylist))
# sum =0
# for i in range (len(mylist)-1): #i=0
#     if i+1 in range(len(mylist)):
#         sum += abs(mylist[i]-mylist[i+1])
# print(sum)
#------------------------------------------------------------------------------------------

#Q9 
# a=50
# b=30
# c=20
# d=10
# print((a+b)*(c/d))#160
# print((a-b)*(c/d))#40
# print(a+(b*c)/d)#110
#------------------------------------------------------------------------------------------

#Q10
# num = 123
# a = num%10 #this will give us the last digit of the number which is 3
# num = num//10 #this will remove the last digit from the number and give us 12
# b = num%10 #this will give us the last digit of the number which is 2
# num = num//10 #this will remove the last digit from the number and give us 1
# c = num%10 #this will give us the last digit of the number which is 1
# rev = a*100 + b*10 + c #this will give us the reverse of the number which is 321
# print(rev) #321
#------------------------------------------------------------------------------------------
#123456 > 654321
# num = 123456
# rev = 0
# while num > 0:
#     a = num % 10 #this will give us the last digit of the number which is 6
#     rev = rev * 10 + a #this will give us the reverse of the number which is 654321
#     num = num // 10 #this will remove the last digit from the number and give us 12345
# print(rev) #654321

# or we can do it without using while loop
# num = 123456
# a = num%10
# num = num//10
# b = num%10
# num = num//10
# c = num%10
# num = num//10
# d = num%10
# num = num//10
# e = num%10
# num = num//10
# f = num%10
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
# print(rev) #654321
#------------------------------------------------------------------------------------------

