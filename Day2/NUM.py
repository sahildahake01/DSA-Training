
#Q1
# num = 123
# a = num%10 #this will give us the last digit of the number which is 3
# num = num//10 #this will remove the last digit from the number and give us 12
# b = num%10 #this will give us the last digit of the number which is 2
# num = num//10 #this will remove the last digit from the number and give us 1
# c = num%10 #this will give us the last digit of the number which is 1
# rev = a*100 + b*10 + c #this will give us the reverse of the number which is 321
# print(rev) #321
#------------------------------------------------------------------------------------------
#123456 > 654321
# num = 123456
# rev = 0
# while num > 0:
#     a = num % 10 #this will give us the last digit of the number which is 6
#     rev = rev * 10 + a #this will give us the reverse of the number which is 654321
#     num = num // 10 #this will remove the last digit from the number and give us 12345
# print(rev) #654321

# or we can do it without using while loop
# num = 123456
# a = num%10
# num = num//10
# b = num%10
# num = num//10
# c = num%10
# num = num//10
# d = num%10
# num = num//10
# e = num%10
# num = num//10
# f = num%10
# rev = a*100000 + b*10000 + c*1000 + d*100 + e*10 + f
# print(rev) #654321
#------------------------------------------------------------------------------------------

#Q2
# Amount = int(input("Enter the amount: "))
# print("100 notes: ", Amount//100)
# print("50 notes: ", (Amount%100)//50) 
# print("20 notes: ", ((Amount%100)%50)//20)
# print("10 notes: ", (((Amount%100)%50)%20)//10)
# print("5 notes: ", ((((Amount%100)%50)%20)%10)//5)
# print("2 coin: ", (((((Amount%100)%50)%20)%10)%5)//2)
# print("1 coin: ", (((((Amount%100)%50)%20)%10)%5)%2)
# sample input: 786
# sample output:
# 100 notes:  7
# 50 notes:  1
# 20 notes:  1
# 10 notes:  1
# 5 notes:  1
# 2 coin:  0
# 1 coin:  1
#------------------------------------------------------------------------------------------