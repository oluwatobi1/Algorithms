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

class BinSearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size +=1
            
    def _put(self, key, val, currentNode):
        if key<currentNode.key:
            if currentNode.hasleftchild():
                self._put(key, val, currentNode.leftchild)
            else:
                currentNode.leftchild = TreeNode(key, val, parent = currentNode)
        else:
            if currentNode.hasrightchild():
                self._put(key, val, currentNode.rightchild)
            else:
                currentNode.rightchild = TreeNode(key, val, parent = currentNode)
                
    def __setitem__(self, k, v):
        self.put(k, v)
        
    def get(self, key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key, currentNode.leftchild)
        elif key>currentNode.key:
            return self._get(key, currentNode.rightchild)
        else:
            print('Node get error')
            
            
    def __getitem__(self, key):
        return self.get(key)
                
                
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
        
        
    def delete(self, key):
        if self.size> 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)
                self.size-=1
            else:
                raise KeyError('Key Not Found')
                
        else:
            if self.size== 1 and self.root.key == key:
                self.root = None
                self.size-=1
            else:
                raise KeyError('Key not found 2')
    def __delitem__(self, key):
        self.delete(key)
        
        
        
    def remove(self, currentnode):
        #for node without children
        if currentnode.isleaf():
            if currentnode.isleftchild():
                currentnode.parent.leftchild = None
            else:
                currentnode.parent.rightchild = None
        #for node with one child that is the left child      
        elif currentnode.hasonechild() and currentnode.hasleftchild():
            if currentnode.isleftchild():
                currentnode.parent.leftchild = currentnode.leftchild
                currentnode.leftchild.parent = currentnode.parent
            elif currentnode.isrightchild():
                currentnode.parent.rightchild = currentnode.leftchild
                currentnode.leftchild.parent = currentnode.parent
                
            else:
                #first
                currentnode.replaceNodeData(currentnode.leftchild.key, currentnode.leftchild.value,
                                           currentnode.leftchild.leftchild, currentnode.leftchild.rightchild)
        #for node with one child that is the rightchild        
        elif currentnode.hasonechild() and currentnode.hasrightchild():
            if currentnode.isrightchild():
                currentnode.parent.rightchild = currentnode.rightchild
                currentnode.rightchild.parent = currentnode.parent
            elif currentnode.isleftchild():
                currentnode.parent.leftchild = currentnode.rightchild
                currentnode.rightchild.parent = currentnode.parent
                
            else: 
                currentnode.replaceNodeData(currentnode.rightchild.key, currrentnode.rightchild.value,
                                           currrentnode.rightchild.leftchild, currrentnode.rightchild.rightchild)
        #for node with both children     
        else:
            if currentnode.hasbothchildren():
                succ = self._findmin(currentnode)
                self.remove(succ)
                currentnode.key = succ.key
                currentnode.value = succ.value
            else:
                print("This is a bug")
    #to             
    def _findmin(self, node):
        node = node.rightchild
        while node.hasleftchild():
            node = node.leftchild
        return node.value
    
    def findmin(self, node):
        while node.hasleftchild():
            node = node.leftchild
        return node.value
        
   #in order traversal #it is recursive cos of __iter__  
    def __iter__(self):
        if self:
            if self.hasleftchild():
                for elem in self.leftchild:
                    yield elem
            yield self.key
            if self.hasrightchild():
                for elem in self.rightchild:
                    yield elem


                
                
                  


t = TreeNode(14,2)

c = TreeNode(20,2)
s = TreeNode(17,3)

c.hasleftchild()

print(t.hasrightchild())

print(t.hasleftchild())