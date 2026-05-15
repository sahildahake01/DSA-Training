# ========================================= BUBBLE SORT =========================================

#Q1
# def bubblesort(arr):
#     for i in range(len(arr)-1): #i used for passes
#         for j in range(len(arr)-i-1): #j=0 start
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#             print(arr)
#         print()

# arr=[64,34,25,12,22,11,90]
# bubblesort(arr)

#-----------------------------------------------------------------------------------------------------------------------
# Q. Security Key Problem  // Repeated numbers count
# arr = [5,7,8,3,7,8,9,2,3]
# new = []
# for i in range(len(arr)):
#     key = arr[i]
#     j = i + 1
#     while j < len(arr):
#         if key == arr[j]:
#             new.append(key)
#             break   
#         j = j + 1
# print(len(new))