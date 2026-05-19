#find the first non repeating character
# def nonRepeating(s):
#     for i in s:
#         if s.count(i)==1:
#             return i
#         print("NO repeating number in string ")
# name = "leetcode"
# result = nonRepeating(name)
# print("The first repeating character is ",result)

#---------------------------------------------------------------------------------------------------

# ip = 7,9,-3,8,-6,-7,8,10
# op  10
# def sum_of_max_product_pair(arr):
#     if len(arr) < 2:
#         return sum(arr) # Handle small lists edge case
        
#     # Sort the array in ascending order
#     # ip becomes: [-7, -6, -3, 7, 8, 8, 9, 10]
#     sorted_arr = sorted(arr)
    
#     # Candidate 1: The two largest numbers (at the end)
#     pos_prod = sorted_arr[-1] * sorted_arr[-2]
    
#     # Candidate 2: The two smallest/most negative numbers (at the start)
#     neg_prod = sorted_arr[0] * sorted_arr[1]
    
#     # Compare the products and return the sum of the winning pair
#     if neg_prod > pos_prod:
#         return sorted_arr[0] + sorted_arr[1]
#     else:
#         return sorted_arr[-1] + sorted_arr[-2]

# # Test with your input
# ip = [7, 9, -3, 8, -6, -7, 8, 10]
# print(sum_of_max_product_pair(ip))  
# # Output: 19 (9 + 10)

#---------------------------------------------------------------------------------------------------
#Array rotation
# arr= [1,2,3,4,5]
# d=2
# n=len(arr)
# op = arr[-d:] + arr[:-d]
# print(op)
# Output: [4, 5, 1, 2, 3]

#---------------------------------------------------------------------------------------------------
#Hackerrank 1
#Q1 Insert a Node at the Tail of a Linked List.
# def insertNodeAtTail(head, data):
#     new_node = SinglyLinkedListNode(data)
    
#     if(head is None):
#         head = new_node
#     else:
#         temp = head
#         while(temp.next is not None):
#             temp = temp.next
#         temp.next = new_node
#         temp = new_node
    
#     return head

#---------------------------------------------------------------------------------------------------
#Hackerrank 2
#Insertion Sort - Part 1
# def insertionSort1(n, arr):
#     e=arr[n-1]
#     for i in range(n-2,-1,-1):
#         if arr[i]<e:
#             arr[i+1]=e
#             print(" ".join(str(x) for x in arr))
#             break
#         else:
#             arr[i+1]=arr[i]
#             print(" ".join(str(x) for x in arr))   
#     else:
#         arr[0]=e
#         print(" ".join(str(x) for x in arr))

#---------------------------------------------------------------------------------------------------
# Hackerrank 3
# Recursive Digit Sum
# def superDigit(n, k):
#     num = str(sum([int(i) for i in str(n)])) * k
#     def rec(num):
#         if len(str(num)) == 1:
#             return num
#         return rec(str(sum([int(i) for i in num])))
#     return rec(num)

#---------------------------------------------------------------------------------------------------
#LEETCODE 1
# sort Colors
# def sortColors(self, nums: List[int]) -> None:
#         for i in range(len(nums)-1): #i used for passes
#             for j in range(len(nums)-i-1): #j=0 start
#                 if nums[j] > nums[j+1]:
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
#             print(nums)