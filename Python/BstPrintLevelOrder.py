class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def levelOrderPrint(node):
    if not node:
        return
    que = [node]
    currentcount = 1
    nextlevel = 0
    l = []
    while len(que)!=0:
        currentnode = que.pop(0)
        currentcount-=1
        l.append(currentnode.val)
        
        if currentnode.right:
            que.append(currentnode.right)
            nextlevel +=1
        if currentnode.left:
            que.append(currentnode.left)
            nextlevel+=1
            
        if currentcount == 0:
            print(l)
            print('\n')
            currentcount, nextlevel = nextlevel, currentcount
            l = []
#testing
a = Node(2)
b = Node(7)
c = Node(3)
d = Node(1)
e = Node(5)
f = Node(8)
g = Node(4)
h = Node(6)

g.left = a #rootnode

a.left = d
a.right = c

g.right = h

h.left = e
h.right = f

f.left = b
levelOrderPrint(g)