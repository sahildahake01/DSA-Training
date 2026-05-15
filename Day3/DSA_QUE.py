# 1
#maximum consecutive ones
# str = [1, 1, 0, 1, 1, 1,0,1,1,1,1]
# count = 0
# max_c = 0
# for i in str:
#     if i == 1:
#         count += 1
#     else:
#         max_c = max(max_c, count)
#         count = 0
# max_c = max(max_c, count)
# print(max_c)
#----------------------------------------------------------------------------------------------------------

#2
# # count substring in a string
# # ip abababab op 4
# str = "abababab"
# count = 0
# print(str.count('ab'))
#----------------------------------------------------------------------------------------------------------

#3
# def findBiggestnumber(SampleArray):
#     biggestNumber = SampleArray[0]              #O(1)
#     for index in range(len(SampleArray)):       #O(n)
#         if SampleArray[index] > biggestNumber:  #O(1)
#             biggestNumber = SampleArray[index]  #O(1)
#     print(biggestNumber)                        #O(1)

# SampleArray = [5,7,9,2,3,4]                     #O(1)
# findBiggestnumber(SampleArray)                  #O(n)
#----------------------------------------------------------------------------------------------------
#========================================= LINEAR SEARCH =========================================
#4
# def linearSearch(array, target):
#     for i in range(0, len(array)):
#         if array[i] == target:
#             return i
#     return -1

# array = [1,2,3,4,8,7,9]
# target = 766
# result = linearSearch(array,target)
# if result == -1:
#     print("Target not Found")
# else:
#     print("Target Found at index: ", result)
#=================================================================================================
#----------------------------------------------------------------------------------------------------

# Q5
# row wise max value
# [[100, 198, 333, 323],
#  [111, 232, 221, 111],
#  [223, 565, 245, 764]]

# arr= [[100, 198, 333, 323],[111, 232, 221, 111],[223, 565, 245, 764]]
# res= []
# for i in range(3):
#     j=0
#     max = arr[i][j]
#     for j in range(4):
#         c_max = arr[i][j]
#         if max < c_max:
#             max = c_max
#     res.append(max)
# print(res)

#---------------------------------------------------------------------------------------------------

#Q6
# input = prashant*is*a*good*programer
# output = ****prashantisagoodprogramer

# name = 'prashant*is*a*good*programer'
# newname = ''
# val=''
# for i in name:
#     if i !='*':
#         newname += i
#     else:
#         val += i
# print(newname)
# print(str(val+newname))

#---------------------------------------------------------------------------------------------------

#Q7  IMP###
# input = aaabbbbccceeeee
# output =a3b4c3e5
# name = 'aaabbbbccceeeee'
# newname = {}
# for i in range(len(name)):
#     key = name[i]
#     count = 0
#     for j in range(len(name)):
#         if key == name[j]:
#             count +=1
#     newname[key] = count
# print(newname)
# for i,j in newname.items():
#     print(i,j,sep='', end='')
#---------------------------------------------------------------------------------------------------

#hackerrank 1
#Complete the function solveMeFirst to compute the sum of two integers.
# def solveMeFirst(a,b):
#     return a+b
# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)    #5

#---------------------------------------------------------------------------------------------------

#hackerrank 2
#removing spaces from string
# city=input("enter your city name: ")
# scity = city.strip()
# if scity == 'Hydrabad':
#     print('hello Hydrabad.. adab')
# elif scity == 'Chennei':
#     print('hello chennei...kem chho ')
# elif scity == 'Banglore':
#     print('hello banglore.. how are you bro')
# else:
#     print('your entered city is invalid')

#---------------------------------------------------------------------------------------------------

#hackerrank 3
#Given an array of integers, find the sum of its elements.

# def simpleArraySum(ar):
#     sum = 0
#     for i in range(len(ar)):
#         sum += ar[i]
#     return sum

#---------------------------------------------------------------------------------------------------

#hackerrank 4
#Compare the Triplets
# def compareTriplets(a, b):
#     alice = 0
#     bob = 0
#     for i,j in zip(range(len(a)),range(len(b))):
#         if a[i]>b[i]:
#             alice +=1
#         if a[i]<b[i]:
#             bob +=1
#         if a[i]== b[i]:
#             pass
#     return alice,bob

#---------------------------------------------------------------------------------------------------

#hackerrank 5
#A Very Big Sum
# def aVeryBigSum(ar):
#     # Write your code here
#     sum = 0
#     for i in range(len(ar)):
#         sum += ar[i]
#     return sum

#---------------------------------------------------------------------------------------------------

#hackerrank 6
# Time Conversion
# def timeConversion(s):
#     hour = s[0:2]
#     remaining = s[2:8]
#     time_format = s[8:10]
#     if time_format == "PM":
#         if int(hour) < 12:
#             hour=int(hour)+12
#         elif int(hour) > 12:
#             hour=int(hour)+1
#     elif time_format == "AM":
#         if int(hour) == 12:
#             hour="00"
#     return(str(hour)+remaining)

#---------------------------------------------------------------------------------------------------

#LEETCODE 1
#1.TWO SUM
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
#         return []

#---------------------------------------------------------------------------------------------------

#LEETCODE 2
#9. Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         reverse = 0
#         xcopy = x
#         while x > 0:
#             reverse = (reverse * 10) + (x % 10)
#             x //= 10
#         return reverse == xcopy

#---------------------------------------------------------------------------------------------------

#LEETCODE 2
#125. Valid Palindrome
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = ''.join(c.lower() for c in s if c.isalnum())
#         left = 0 
#         right = len(s) - 1

#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1

#         return True

#---------------------------------------------------------------------------------------------------

#HACHEREARTH 1
#Roy and Profile Picture
# L = int(input()) 
# N = int(input())

# for _ in range(N):
#     W, H = map(int, input().split())
    
#     if W < L or H < L:
#         print("UPLOAD ANOTHER")
#     elif W == H:
#         print("ACCEPTED")
#     else:
#         print("CROP IT")
