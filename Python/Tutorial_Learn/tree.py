class BinaryTree():
    
    def __init__(self, root) -> None:
        self.root = root
        self.leftchild = None
        self.rightchild = None

    def insertLeft(self, leftchild):
        if not self.leftchild:
            self.leftchild = BinaryTree(leftchild)
        else:
            temp = BinaryTree(self.leftchild)
            temp.leftchild = self.leftchild
            self.leftchild = temp

    
    def insertRight(self, rightchild):
        if not self.rightchild:
            self.rightchild = BinaryTree(rightchild)
        else:
            temp = BinaryTree(self.rightchild)
            temp.rightchild = self.rightchild
            self.rightchild = temp
    def getRightChild(self):
        return self.rightchild

    def getLeftChild(self):
        return self.leftchild

    def setRootVal(self, key):
        self.root = key

    def getRootVal(self):
        return self.root

b =BinaryTree("a")
print(b.getRootVal())
    



