# ========================================= BINARY-SEARCH =========================================
# -Binary search a faster than linear search
# -half of the remaining element can be eliminated at a time. insted of elimanating them one by one
# -binary search only works for sorted array

#Q1--
# def binarysearch(arr,target):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         mid = int((low+high)/2)
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
            
# arr = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target = 72
# result= binarysearch(arr, target)
# if result == -1:
#     print("element not found")
# else:
#     print("element found at ",result)
# #element found at  30
#-----------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------

#LEETCODE
#704. Binary Search
# class Solution(object):
#     def search(self, nums, target):
#         l = 0
#         h = len(nums) - 1
#         while l <= h:
#             m = (l + h) // 2
#             if nums[m] == target:
#                 return m
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 h = m - 1
#         return -1

#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------
