# ========================================= STACK =========================================
# stack implementation without size limit
# stack implementation with size limit

# there are two ways 
#1. list/array
#2. linklist

#Stack using list:
#   easy to implement
#   speed problem when it grow
#
#Stack using Linklist:
#   fast performance
#   implementation is not easy

#---------------------------------------------------------------------------------------------------
#Implementation without limit
#1
# import sys
# class Stack:
#     def __init__(self):
#         self.mystack =[]

#     def push(self,value):
#         self.mystack.append(value)
#         print("Element pushed to Stack..")
        
#     def display(self):
#         print(self.mystack)

#     def isEmpty(self): 
#         if self.mystack == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.mystack.pop())

#     def peak(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.mystack[-1])
    
#     def deletestack(self):
#         self.mystack = None

# obj = Stack()
# print("Stack has created: ")
# while True:
#     print("1. PUSH OPRATION")
#     print("2. DISPLAY STACK")
#     print("3. POP OPRATION")
#     print("4. PEAK OPRATION")#only returns top element doesn't delete
#     print("5. DELETE STACK")
#     print("7. EXIT")
#     choice = int(input("Enter your Choice: "))
#     if choice == 1:
#         value = int(input("Enter value to push in Stack: "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peak()
#     elif choice == 5:
#         obj.deletestack()
#     else:
#         sys.exit()

#-----------------------------------------------------------------------------------------------------------------------

#Implementation with limit
#2
# import sys
# class Stack:
#     def __init__(self,size):
#         self.mystack =[]#creating stack
#         self.Stacksize = size

#     def isFUll(self):
#         if len(self.mystack) == self.Stacksize:
#             return True
#         else:
#             return False

#     def push(self,value):
#         if self.isFUll():
#             print("Stack is full..")
#         else:
#             self.mystack.append(value)
#             print("Element pushed to Stack..")
        
#     def display(self):
#         print(self.mystack)

#     def isEmpty(self):
#         if self.mystack == []:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.mystack.pop())

#     def peak(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.mystack[-1])
    
#     def deletestack(self):
#         self.mystack = None

# size = int(input("Enter the size of stack: "))
# obj = Stack(size)
# print("Stack has created: ")
# while True:
#     print("1. PUSH OPRATION")
#     print("2. DISPLAY STACK")
#     print("3. POP OPRATION")
#     print("4. PEAK OPRATION")#only returns top element doesn't delete
#     print("5. DELETE STACK")
#     print("7. EXIT")
#     choice = int(input("Enter your Choice: "))
#     if choice == 1:
#         value = int(input("Enter value to push in Stack: "))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peak()
#     elif choice == 5:
#         obj.deletestack()
#     else:
#         sys.exit()

#-----------------------------------------------------------------------------------------------------------------------

#Q3
#count of specific digit
# mylist = [5,7,2,3,7,8,2,3,3]
# newdict ={}
# for i in range(len(mylist)):
#     count =0
#     key = mylist[i]
#     j = 1
#     while j<len(mylist):
#         if key == mylist[j]:
#             count+=1
#         j = j+1
#     if count>1:
#         newdict[key]= count

# max = newdict
# print(max)    #{7: 2, 2: 2, 3: 3}

#-----------------------------------------------------------------------------------------------------------------------

#Q4

#student number

#-----------------------------------------------------------------------------------------------------------------------

#Q5
# input
# 8
# 79,77,54,81,48,34,25,16
# output
# 3
# Ch
# import math
# arr = [79,77,54,81,48,34,25,16]
# c =0
# for i in range(len(arr)):
#     if math.sqrt(arr[i]) %1 == 0:
#         c += 1
# print(c)

