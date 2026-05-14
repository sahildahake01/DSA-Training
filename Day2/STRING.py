# String in Python
# name = "prashantjha" #string 
#        #123456789
# print(name[0]) #p
# print(name[1]) #r
# print(name[-1]) #a
# #string slicing
# print(name[0:5]) #prash
# print(name[1:]) #rashantjha
# print(name[:5]) #prash
# print(name[:]) #prashantjha
# print(name[1:8:2]) #rshnj
# print(name[::-1]) #ahjtnahsrp
#--------------------------------------------------------------------------------------------------

#String Methods
# s = "Python is high level programming language"
# print(s.lower()) #python is high level programming language
# print(s.upper()) #PYTHON IS HIGH LEVEL PROGRAMMING LANGUAGE
# print(s.swapcase()) #pYTHON IS HIGH LEVEL PROGRAMMING LANGUAGE  
# print(s.title()) #Python Is High Level Programming Language
# print(s.capitalize()) #Python is high level programming language
#---------------------------------------------------------------------------------------------------

#String Formatting
# name = "prashant"
# sal = 5000
# age = 28
# print("{} sal is {} and age is {}".format(name,sal,age)) #prashant sal is 5000 and age is 28
# print("{0} sal is {1} and age is {2}".format(name,sal,age)) #prashant sal is 5000 and age is 28
# print("{x} sal is {y} and age is {z}".format(x=name,y=sal,z=age)) #prashant sal is 5000 and age is 28
# A=1
# print(f"{name} is a good boy") #prashant is a good boy
#---------------------------------------------------------------------------------------------------

#Iterating through a string
# name = "prashant"
# for i in name:
#     print(i) #print each character in new line
#---------------------------------------------------------------------------------------------------

#remove duplicate character from string
# name = "prashant"
# newname =""
# for i in name:
#     if i not in newname:
#         newname += i
# print(newname)
#---------------------------------------------------------------------------------------------------

#reverse string
# name = "prashant"
# newname = ""
# N=len(name)
# for i in range(N-1,-1,-1):
#         newname += name[i]
# print(newname)
#---------------------------------------------------------------------------------------------------

#palindrome string
# name = "help4code"
# print(name)
# print(name[::-1]) #right to left
# if name == name[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome ")
#---------------------------------------------------------------------------------------------------

#Anagram string
# name1 = "listen"
# name2 = "silent"
# if sorted(name1) == sorted(name2):
#     print("anagram")
# else:
#     print("not anagram")
#---------------------------------------------------------------------------------------------------

#count vowels and consonants in a string
# vowels = "aeiou"
# name = "hello"
# cons = 0
# vov = 0
# for i in name:
#     if i in vowels:
#         vov += 1
#     else:
#         cons += 1
# print("consonants:",cons)
# print("vowels:",vov)

#---------------------------------------------------------------------------------------------------
#pangram string
# s = "The quick brown fox jumps over the lazy dog"
# s = s.lower()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     if char not in s:
#         print("not pangram")
#         break
# else:
#     print("pangram")
#---------------------------------------------------------------------------------------------------

#count words in string
# name = "sahil is good boy and karan is int"
# c = 0
# d = 0
# for i in name:
#     c = name.count(" ")+1
# print(c)

#---------------------------------------------------------------------------------------------------

#count special character in string
# s = input()
# count = 0
# for ch in s:
#     if not ('a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9'):
#         count += 1
# print(count)
#---------------------------------------------------------------------------------------------------

#uppercase conversion
# s= "sahil is the best person"
# print(s.title())
#---------------------------------------------------------------------------------------------------

#string validation
# print("prashantjha777".isalnum()) #True
# print("prashantjha".isalpha()) #True
# print("77776".isdigit()) #True
# print("sdsdsdsd".islower()) #True
# print(''.islower()) #False
# print("SDSDSDSD".isupper()) #True
# print('My Name Is Sahil'.istitle()) #False
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))
#---------------------------------------------------------------------------------------------------

#string searching
# print("Prashant".find("r"))
# print("Prasahnt".index("r"))
# print("Prashant jha".count("a"))
#---------------------------------------------------------------------------------------------------

#Nested loop
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end="  ")
#     print()
#---------------------------------------------------------------------------------------------------
#pattern printing
# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end="  ")
#     print()
#SAMPLE OUTPUT
# enter the number of rows: 5
# A  A  A  A  A
# B  B  B  B  B
# C  C  C  C  C
# D  D  D  D  D
# E  E  E  E  E
#---------------------------------------------------------------------------------------------------

#
# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end="  ")
#     print()
#SAMPLE OUTPUT
# enter the number of rows: 5
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
#---------------------------------------------------------------------------------------------------

# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+i),end="  ")
#     print()
#SAMPLE OUTPUT
# enter the number of rows: 5
# A  A  A  A  A
# B  B  B  B
# C  C  C
# D  D
# E
#---------------------------------------------------------------------------------------------------

# import time
# n = int(input("Enter number of rows: "))
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, i+1):
#         time.sleep(1)
#         print("*", end=" ")
#     print()
#----------------------------------------------------------------------------------------------------

#input [1,2,3,4,]
#output [24, 12, 8, 6]
#product of array except self
# arr = [1, 2, 3, 4]
# n = len(arr)
# output = [1] * n
# for i in range(1, n):
#     output[i] = output[i - 1] * arr[i - 1]
# temp = 1
# for i in range(n - 1, -1, -1):
#     output[i] *= temp
#     temp *= arr[i]
# print(output)
#---------------------------------------------------------------------------------------------------


