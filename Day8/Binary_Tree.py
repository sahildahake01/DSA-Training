#============================== BINARY TREE ==============================

# >>Full binary tree >>
# - each node has either 0 or 2 children
# - no node has a single child

# >>Complete binary tree >>
# - All levels except possibly the last are completly filled
# - Nodes in the last level are filled from left to right

# >>Perfect Binary >>
# - All internal nodes have exactly two nodes
# - all leaf node at same level

#-------------------------------------------------------------------
#                     N1

#              N2           N3

#        N4       N5   N6       N7

#   N9       N10

# >Postorder - N9 > N10 > N4 > N5 > N2 > N6 > N7 > N3 >N1
# leaf Subtree >> Root node >> Right Subtree 

# level order traversal
# level1:   N1
# level2:   N2,N3
# level3:   N4,N5,N6,N7
# level4:   N9,N10
# Final- N1>N2>N3>N4>N5>N6>N7>N9>N10
#-------------------------------------------------------------------


# Why Binary Search Tree?
# It perform faster than binary tree when inserting and deleting node.

#-----------------------------------------------------------------------------------------------------------------------

#Q1
#                       70

#              50               90

#        30       60       80       100

#   20       40                  95

#10

# Inorder (Left → Root → Right)     >10 20 30 40 50 60 70 80 90 95 100
# Preorder (Root → Left → Right)    >70 50 30 20 10 40 60 90 80 100 95
# Postorder (Left → Right → Root)   >10 20 40 30 60 50 80 95 100 90 70
#---------------------------------------------------
import sys
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insertNode(rootnode, nodevalue):
    if rootnode.data == None:
        rootnode.data = nodevalue

    elif nodevalue <= rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BSTNode(nodevalue)
        else:
            insertNode(rootnode.leftchild, nodevalue)

    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BSTNode(nodevalue)
        else:
            insertNode(rootnode.rightchild, nodevalue)


def preOrderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data,end=' ')
    preOrderTraversal(rootnode.leftchild)
    preOrderTraversal(rootnode.rightchild)

def inOrderTraversal(rootnode):
    if not rootnode:
        return
    inOrderTraversal(rootnode.leftchild)
    print(rootnode.data,end=' ')
    inOrderTraversal(rootnode.rightchild)

def postOrderTraversal(rootnode):
    if not rootnode:
        return
    postOrderTraversal(rootnode.leftchild)
    postOrderTraversal(rootnode.rightchild)
    print(rootnode.data,end=' ')

def searchNode(rootnode, nodevalue):
    if rootnode.data == nodevalue:
        print("The value is Root Node")

    elif nodevalue < rootnode.data:
        if rootnode.leftchild is None:
            print("Value not found")
        elif rootnode.leftchild.data == nodevalue:
            print(f"{nodevalue} is on the LEFT side of {rootnode.data}")
        else:
            searchNode(rootnode.leftchild, nodevalue)

    else:
        if rootnode.rightchild is None:
            print("Value not found")
        elif rootnode.rightchild.data == nodevalue:
            print(f"{nodevalue} is on the RIGHT side of {rootnode.data}")
        else:
            searchNode(rootnode.rightchild, nodevalue)

newBST = BSTNode(70)

insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
insertNode(newBST, 95)
insertNode(newBST, 10)

# print()
# preOrderTraversal(newBST)
# print('\n')
# print('Inorder')
# inOrderTraversal(newBST)
# print('\n')
# print('Postorder')
# postOrderTraversal(newBST)
# print('\n')
# searchNode(newBST,20)

while True:
    print()
    print("==================")
    print("1. Insert node")
    print("2. PreOrder Traversal")
    print("3. InOrder Traversal")
    print("4. PostOrder Traversal")
    print("5. Search Node")
    print("6. EXIT")
    print("==================")

    choice = int(input("Enter your Choice: "))
    if choice == 1:
        nodevalue = int(input("Enter Node to add: "))
        insertNode(newBST, nodevalue)
    elif choice == 2:
        print('Preorder-')
        preOrderTraversal(newBST)
    elif choice == 3:
        print('Inorder-')
        inOrderTraversal(newBST)
    elif choice == 4:
        print('Postorder-')
        postOrderTraversal(newBST)
    elif choice == 5:
        nodevalue=int(input('Enter node to find:'))
        searchNode(newBST,nodevalue)
    else:
        sys.exit()



