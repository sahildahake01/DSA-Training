#linklist 

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

# linkedlist = Linkedlist()

# linkedlist.head = Node( 5)
# second          = Node(10)
# Third           = Node(15)
# Fourth          = Node(20)
# Fifth           = Node(25)

# linkedlist.head.next = second
# second.next = Third
# Third.next  = Fourth
# Fourth.next = Fifth

# while linkedlist.head != None:
#     print('|',linkedlist.head.data,'|','-->',end=' ')
#     linkedlist.head = linkedlist.head.next
#op= | 5 | --> | 10 | --> | 15 | --> | 20 | --> | 25 | --> 
#---------------------------------------------------------------------------------------

# import sys
# class Node:
#     def __init__(self,data):
#         self.data = data        #instance variable
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def addnode(self,value):
#         self.node = Node(value)
#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.tail.next = self.node
#             self.tail      = self.node

#     def add_beg(self,value):
#         self.node = Node(value)
#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.node.next = self.head
#             self.head      = self.node

#     def add_in_bet(self,position,value):
#         position -= 1
#         if position == 0:
#             self.add_beg(value)
#             return

#         self.node = Node(value)
#         current = self.head
        
#         # Traverse to the node just before the insertion position
#         for _ in range(position - 1):
#             if current is None:
#                 print("Position out of bounds.")
#                 return
#             current = current.next

#         if current is None:
#             print("Position out of bounds.")
#             return

#         self.node.next = current.next
#         current.next   = self.node

#         # Update tail if we inserted at the very end
#         if self.node.next is None:
#             self.tail = self.node



#     # def add_end(value):

#     def display(self):
#         if not self.head:
#             print("LinkedList is empty.")
#             return
#         current = self.head
#         while current: 
#             print(current.data, end=" -> ")
#             current = current.next
            

# if __name__ == "__main__":
#     object = Linkedlist()
#     while True:
#         print('1. Add Node Linkedlist')
#         print('2. Add Node at Begining')
#         print('3. Add Node in between')
#         print('4. Add Node at END')
#         print('5. DISPLAY LINKED-LIST')
#         print('6. EXIT')
#         ch = int(input('Enter your Choice - '))

#         if ch == 1:
#             value = int(input("Enter value to ADD to Linkedlist: "))
#             object.addnode(value)
#             print('Node added successfully in single Linkedlist.')
#         elif ch == 2:
#             value = int(input("Enter value to ADD to Linkedlist: "))
#             object.add_beg(value)
#             print('Node added successfully at Begining..')
#         elif ch == 3:
#             position = int(input("Enter Position : "))
#             value = int(input("Enter value to ADD to Linkedlist: "))
#             object.add_in_bet(position,value)
#             print('Node added successfully in between given nodes ')
#         # elif ch == 4:
#         #     value = int(input("Enter value to ADD to Linkedlist: "))
#         #     object.add_end(value)
#         #     print('Node added successfully at end')
#         elif ch == 5:
#             object.display()
#         else:
#             sys.exit()

#---------------------------------------------------------------------------------------------------