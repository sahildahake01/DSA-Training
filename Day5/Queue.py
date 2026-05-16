# ========================================= QUEUE =========================================
# without and with limit
# 1. EnQueue
# 2. DeQueue
# 3. Display Queue
# 4. isEmpty
# 5. isFull
# 6. Peak

#Queue using list
#   easy to implement
#   speed problem when i grows
#
#Queue using linklist
#   fast performance
#   implementation is not easy #
#------------------------------------------------------------------------------------------

# import sys
# class Queue:
#     def __init__(self,size):
#         self.myQueue =[] #creating empty Queue
#         self.QueueSize =size #queue size defined

#     def isFull(self):
#         if len(self.myQueue) == self.QueueSize:
#             return True
#         else:
#             return False
        
#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False

#     def enqueue(self,value):
#         if self.isFull():
#             print("Queue is full..")
#         else:
#             self.myQueue.append(value)
#             print("Element Added to Queue...")

#     def dequeue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print(self.myQueue.pop(0))

#     def display(self):
#         print(self.myQueue)

#     def peek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print(self.myQueue[0])
    
#     def deletequeue(self):
#         self.myQueue = None


# size = int(input("Enter the size of Queue: "))
# obj = Queue(size)
# print("Queue is created..")

# while True:
#     print()
#     print("==================")
#     print("1. EnQueue")
#     print("2. DeQueue")
#     print("3. DISPLAY QUEUE")
#     print("4. PEEK OPRATION")#only returns top element doesn't delete
#     print("5. DELETE QUEUE")
#     print("6. EXIT")
#     print("==================")

#     choice = int(input("Enter your Choice: "))
#     if choice == 1:
#         value = int(input("Enter value to ADD in Queue: "))
#         obj.enqueue(value)
#     elif choice == 2:
#         obj.dequeue()
#     elif choice == 3:
#         obj.display()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deletequeue()
#     else:
#         sys.exit()


