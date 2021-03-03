def BinaryTree(r):
    return [r, [],[]]

def insertLeft(r, item):
    t = r.pop(1)

    if len(t)>1:
        r.insert(1, [item, t, []])
    else:
        r.insert(1, [item, [], []])

def insertRight(r, item):
    t = r.pop(2)

    if len(t)>1:
        r.insert(2, [item, [], t])
    else:
        r.insert(2, [item, [], []])

def getRootval(r):
    return r[0]

def setRootval(r, newVal):
    r[0]=newVal

def getLeftChild(r):
    return r[1]
def getRightChild(r):
    return r[2]

def getTree(r):
    return r
    


r = BinaryTree(1)
print(getTree(r))
insertLeft(r, 3)
insertLeft(r, 5)
print(getTree(r))
insertRight(r, 2)
insertRight(r, 88)
print(getTree(r))