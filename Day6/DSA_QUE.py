#Q1
# n=input('given string: ')   #given string: asdfgh
# rev= ''
# for i in str(n):
#     rev=i + rev
# print(rev)                  #hgfdsa

#-----------------------------------------------------------------------------------------------------------------------

# # Q2: Corrected Valid Parentheses Logic
# def is_valid(s: str) -> bool:
#     stc = []
    
#     for i in range(len(s)):
#         # If it is an opening bracket, push it to the stack
#         if s[i] == '(' or s[i] == '{' or s[i] == '[':
#             stc.append(s[i])
#         else:
#             # If stack is empty but we see a closing bracket, it's invalid
#             if not stc:
#                 return False
            
#             top = stc.pop()
#             # Check for mismatched pairs
#             if s[i] == ')' and top != '(':
#                 return False
#             if s[i] == ']' and top != '[':
#                 return False
#             if s[i] == '}' and top != '{':
#                 return False
                
#     # The string is valid only if the stack is completely empty at the end
#     return len(stc) == 0

# # Test the function
# strr = "{[()]}"
# print('Is Valid -',is_valid(strr)) # Output: True

#-----------------------------------------------------------------------------------------------------------------------

#print duplicate elements
# list=[4,3,2,7,8,2,1,5,5]
# dict={}
# Result =[]
# for i in list:
#     if i in dict:
#         Result.append(i)
#     else:
#         dict[i] = 1
# print(Result)

#-----------------------------------------------------------------------------------------------------------------------

#sort dictionary by key or value:
# dict = {'C': 3, 'B': 2, 'A': 1}
# for _ in sorted(dict):
#     print(dict[_]) #print key and value in sorted order of keys
# op is 1 2 3

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------

