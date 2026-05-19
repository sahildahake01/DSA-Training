#================================== TREE ========================================
# implemented by using linklist,array,list
#--------------------------------------------------------------------------------
# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child =[]

#     def __str__(self,level = 0):
#         ret ="    "* level+ str(self.data) + "\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret

#     def addchild(self,object):
#         self.child.append(object)
#         print('tree node added')

# rootnode = Tree('Drinks')
# Hot      = Tree('Hot')
# Cold     = Tree('Cold')
# Tea      = Tree('Tea')
# Cofee    = Tree('Cofee')
# Nonalcoholic= Tree('NonAlcoholic')
# Alcohol  = Tree('Alcohol')

# rootnode.addchild(Hot)
# rootnode.addchild(Cold)
# Hot.addchild(Tea)
# Hot.addchild(Cofee)
# Cold.addchild(Nonalcoholic)
# Cold.addchild(Alcohol)

# print(rootnode)

#---------------------------------------------------------------------------------------------------
# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.child =[]

#     def __str__(self,level = 0):
#         ret ="  "* level+ str(self.data) + "\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret

#     def addchild(self,object):
#         self.child.append(object)
#         print('tree node added')

# rootnode = Tree('N1')
# N2       = Tree('N2')
# N3       = Tree('N3')
# N4       = Tree('N4')
# N5       = Tree('N5')
# N6       = Tree('N6')
# N7       = Tree('N7')
# N8       = Tree('N8')

# rootnode.addchild(N2)
# rootnode.addchild(N3)
# N2.addchild(N4)
# N2.addchild(N5)
# N3.addchild(N6)
# N4.addchild(N7)
# N4.addchild(N8)

# print(rootnode)