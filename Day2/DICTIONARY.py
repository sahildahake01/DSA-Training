# mydict = {101: 'Sahil', 102: 'Ashish', "103": 'Rahul', "104": 'Sandip', 101: 'Sandip', 104: 'Ashish'}
# print(mydict) # this will print the dictionary with unique keys, duplicate keys will be overwritten
# op is {101: 'Sandip', 102: 'Ashish', '103': 'Rahul', 104: 'Ashish'}

# a= mydict[102] # key 102 -->value 'Ashish'
# print(a)
# op is Ashish

# mydict[102]="peter"
# print(mydict) # updated value for key 102
# op is {101: 'Sandip', 102: 'peter', '103 ': 'Rahul', 104: 'Ashish'}

# for x in mydict:
#     print(x) #prints key
# op is 101, 102, 103, 104

# for x in mydict.values():
#     print(x) #print values
# op is Sandip, Ashish, Rahul, Sandip, Ashish

# for x,y in mydict.items():
#     print(x,y) # print key and value
# op = 101 Sandip  102 Ashish   103 Rahul   104 Sandip  104 Ashish   

#adding new key value pair in the dictionary
# mydict['phone_no'] = 1234567890
# print(mydict) #print updated dictionary with new key value pair
# op is {101: 'Sandip', 102: 'Ashish', '103': 'Rahul', '104': 'Sandip', 104: 'Ashish', 'phone_no': 1234567890}

# mydict.pop(101)
# print(mydict) # remove the key 101 and its value from the dictionary
# op is {102: 'Ashish', '103': 'Rahul', '104': 'Sandip', 104: 'Ashish', 'phone_no': 1234567890}
#-----------------------------------------------------------------------------------------------------------------------

#Q1
# a={(1,2):1, (2,3):2, (4,5):3}
# print(a[4,5]) #print tuple as key and integer as value
# op is 3
#-----------------------------------------------------------------------------------------------------------------------

#Q2
# a = {'a':1, 'b':2, 'c':3}
# print(a['a','b']) 
# this will give an error because we are trying to access the value of a key that is a
# tuple ('a','b') which does not exist in the dictionary
# op is KeyError: ('a', 'b')
#-----------------------------------------------------------------------------------------------------------------------

#Q3
# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print(arr) #prints updated value for key 1
# # op is {1: 2, '1': 2}
# sum =0
# for k in arr:
#     sum += arr[k]
# print(sum) #print sum of values
# op is 4
#-----------------------------------------------------------------------------------------------------------------------

#Q4
# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4
# print(my_dict) #prints three key value pairs
# # op is {1: 4, '1': 2}
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum) # this will print the sum of values in the dictionary 
# op is 6
#-----------------------------------------------------------------------------------------------------------------------

#Q5
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(4,3)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum) # this will print the sum of values in the dictionary
# # op is 30
# print(my_dict) # this will print the dictionary with tuple as key and integer as value
# op is {(1, 2, 4): 8, (4, 2, 1): 10, (4, 3): 12}
#-----------------------------------------------------------------------------------------------------------------------

#Q6
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box])) 
# this will give an error because we are trying to access the value of a key 
# that is a dictionary (box) which is not hashable and cannot be used as a key in another dictionary (crates)
# op is TypeError: unhashable type: 'dict'
#-----------------------------------------------------------------------------------------------------------------------

#Q7
# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print(dict[_]) #print key and value in sorted order of keys
# # op is 96, 98, 97
#-----------------------------------------------------------------------------------------------------------------------

#Q8
# rec = {"Name": "Prashant", "Age": 25}
# r = rec.copy() # create a shallow copy of rec
# print(id(r) == id(rec)) #print False because r and rec are two different objects in memory
# # op is False
# print(id(r))
# print(id(rec))    # op is different memory addresses for r and rec
#-----------------------------------------------------------------------------------------------------------------------

#Q9
# rec = {"Name": "Python", "Age": 25, 'address': 'ngp, 'country': 'India'}
# id1 = id(rec)
# del rec
# rec = {"Name": "Python", "Age": 25, 'address': 'ngp', 'country': 'India'} 
# id2 = id(rec)
# print(id1 == id2) # this will print False because the two dictionaries are different objects in memory
# op is False
# print(id1)
# print(id2)
# op is different memory addresses for id1 and id2
#-----------------------------------------------------------------------------------------------------------------------

#Q10    finding the max value in the dictionary
# dict = {'a': 1, 'b': 2, 'c': 3}
# max_value = max(dict.values()) # maximum value
# print(max_value) # this will print the maximum value in the dictionary
# # op is 3
#-----------------------------------------------------------------------------------------------------------------------

#Q11   finding the key with the minimum value in the dictionary
# dict = {'X': 20, 'Y': 10, 'Z': 30}
# min_key = min(dict, key=dict.get)
# print(min_key) 
# # op is 'Y'
#-----------------------------------------------------------------------------------------------------------------------

#Q12 count frequency of elements in a string using dictionary
# dict = {}
# no = 2,3,6,1,7,5,3,7,5,2
# for num in no: # iterate through the tuple of numbers
#     if num in dict: # check if the number is already a key in the dictionary
#         dict[num] += 1 # if it is, increment its value by 1
#     else:
#         dict[num] = 1 # if it is not, add it to the dictionary with a value of 1
# print(dict) # op is {2: 2, 3: 2, 6: 1, 1: 1, 7: 2, 5: 2}




