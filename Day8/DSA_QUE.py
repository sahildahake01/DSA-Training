# Q1
# find first zeros and remove it.
# list =input()
# for i in range(2,len(list)):
#     print(list[i], end=' ')

#---------------------------------------------------------------------------------------------------
# Q2
# find the first missing positive integer
# def firstMissingPositive(nums):
#     n = len(nums)
#     # 1. Rearrangement Phase
#     for i in range(n):
#         # While loop is key to swap until the correct value is in place
#         while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
#             # Correct index for value x is x-1
#             correct_idx = nums[i] - 1
#             nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            
#     # 2. Scanning Phase
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1
            
#     # 3. If all present
#     return n + 1

# def first_missing_positive(nums):
#     n = len(nums)
    
#     # 1. In-place swap (Cyclic Sort)
#     for i in range(n):
#         while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
#             j = nums[i] - 1
#             nums[i], nums[j] = nums[j], nums[i]
            
#     print(f"Sorted array: {nums}")
    
#     # 2. Find missing value
#     for i, val in enumerate(nums):
#         if val != i + 1:
#             return i + 1
#     return n + 1

# nums = [3, 4, -1, 1]
# ans = first_missing_positive(nums)
# print(f"Missing value: {ans}") #2

#---------------------------------------------------------------------------------------------------
# Hackerrank 1
# Print the Elements of a Linked List
# def printLinkedList(head):
#     if not head:
#         print("LinkedList is empty.")
#         return
#     current = head
#     while current: 
#         print(current.data)
#         current = current.next

#---------------------------------------------------------------------------------------------------
# Hackerrank 2
# Left Rotation
# def rotateLeft(d, arr):
#     return  arr[d:] + arr[:d]

#---------------------------------------------------------------------------------------------------
# LEETCODE 1
# 121. Best Time to Buy and Sell Stock
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy_price = prices[0]
#         profit = 0
#         for p in prices[1:]:
#             if buy_price > p:
#                 buy_price = p
#             profit = max(profit, p - buy_price)
#         return profit
#---------------------------------------------------------------------------------------------------
# LEETCODE 2
#9. Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == (str(x))[::-1]

#---------------------------------------------------------------------------------------------------
# LEETCODE 2
#46. Permutations
# class Solution:
#     def permute(self, l: List[int]) -> List[List[int]]:
#         def dfs(path, used, res):
#             if len(path) == len(l):
#                 res.append(path[:]) # note [:] make a deep copy since otherwise we'd be append the same list over and over
#                 return

#             for i, letter in enumerate(l):
#                 # skip used letters
#                 if used[i]:
#                     continue
#                 # add letter to permutation, mark letter as used
#                 path.append(letter)
#                 used[i] = True
#                 dfs(path, used, res)
#                 # remove letter from permutation, mark letter as unused
#                 path.pop()
#                 used[i] = False
            
#         res = []
#         dfs([], [False] * len(l), res)
#         return res

#---------------------------------------------------------------------------------------------------
# LEETCODE 3
# 39. Combination Sum
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.ans = []                                   # for adding all the answers
#         def traverse(candid, arr,sm):                   # arr : an array that contains the accused combination; sm : is the sum of all elements of arr 
#             if sm == target: self.ans.append(arr)       # If sum is equal to target then you know it, I know it, what to do
#             if sm >= target: return                     # If sum is greater than target then no need to move further.
#             for i in range(len(candid)):                # we will traverse each element from the array.
#                 traverse(candid[i:], arr + [candid[i]], sm+candid[i])   #most important, splice the array including the current index, splicing in order to handle the duplicates.
#         traverse(candidates,[], 0)
#         return self.ans

#---------------------------------------------------------------------------------------------------
