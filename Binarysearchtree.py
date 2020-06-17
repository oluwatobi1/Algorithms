class TreeNode:
    
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
        
    def hasleftchild(self):
        return self.leftchild
    def hasrightchild(self):
        return self.rightchild
    def isleftchild(self):
        return self.parent and self.parent.leftchild == self
    
    def isrightchild(self):
        return self.parent and self.parent.rightchild == self
    
    def isroot(self):
        return not self.parent
    
    def isleaf(self):
        return not (self.leftchild or self.rightchild)
    def hasanychildren(self):
        return self.leftchild or self.rightchild
    
    def hasonechild(self):
        return ((self.leftchild or self.rightchild) and not(self.hasbothchildren()))
    
    def hasbothchildren(self):
        return self.leftchild and self.rightchild
    def replaceNodeData(self, key, value, left, right,parent):
        self.key = key
        self.payload = value
        self.leftchild = left
        self.rightchild = right
        self.parent = parent
    


t = TreeNode(14,2)

c = TreeNode(20,2)
s = TreeNode(17,3)

c.hasleftchild()

print(t.hasrightchild())

print(t.hasleftchild())