#=============================================RECURSION=============================================

# uses stack
# not memory efficient
# iteration is space efficient
# less time efficient

# when to use recursion?
# when the main problem can be divided into similar sub-problem, then we use recursion.

#---------------------------------------------------------------------------------------------------
#find factorial of number
# def Factorial(num):
#     if num <=1:
#         return 1
#     return num*Factorial(num-1)
# print(Factorial(4)) #24

#---------------------------------------------------------------------------------------------------
#capitalized First letter of word in list
# def capitalizedFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
    
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalizedFirst(arr[1:])
# print(capitalizedFirst(['car','taco','banana']))

#---------------------------------------------------------------------------------------------------
#calculate power
# def Power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base * Power(base, exponent-1)

# print(Power(2,0))   #1
# print(Power(2,2))   #4
# print(Power(2,4))   #16

#---------------------------------------------------------------------------------------------------
# find the product of array using recursion
# def productArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0]* productArray(arr[1:])#starts from index 1 and moves forward

# print(productArray([1,2,3]))    #6
# print(productArray([1,2,3,10])) #60

#---------------------------------------------------------------------------------------------------
# reverse the string
# def reverse(strr):
#     if len(strr) <= 1:
#         return strr
#     return strr[len(strr)-1] + reverse(strr[0:len(strr)-1])

# print(reverse('nohtyp'))        #python
# print(reverse('vanamidaA'))     #aadimanav

#---------------------------------------------------------------------------------------------------
# find recursive range
# def recursiveRange(num):
#     if num <= 0:
#         return 0
#     return num + recursiveRange(num-1)

# print(recursiveRange(6)) #21

#---------------------------------------------------------------------------------------------------
# check palindrome using recursion
# def Palindrome(strr):
#     if len(strr) == 0:
#         return True
#     if strr[0] != strr[len(strr)-1]:
#         return False
#     return Palindrome(strr[1:-1])

# print(Palindrome('awesome'))

#---------------------------------------------------------------------------------------------------
# 
# def someRecursive(arr,cb):
#     if len(arr) == 0:
#         return False
#     if not (cb(arr[0])):
#         return someRecursive(arr[1:],cb)
#     return True

# def isOdd(num):
#     if num%2 ==0:
#         return False
#     else:
#         return True

# print(someRecursive([1,2,3,4], isOdd))  #true
# print(someRecursive([4,6,8,9], isOdd))  #true
# print(someRecursive([4,6,8], isOdd))    #false

#---------------------------------------------------------------------------------------------------# 
