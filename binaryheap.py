class BinHeap:
    def __init__(self):
        self.Heap = [0]
        self.currentsize = 0
        
    
    def move(self, indx):
        
        while indx//2>0:
            print(indx, 'index')
            if self.Heap[indx//2]>self.Heap[indx]:
                tmp = self.Heap[indx]
                self.Heap[indx] = self.Heap[indx//2]
                self.Heap[indx//2] = tmp
            indx = indx//2
    
    def insert(self, item):
        self.Heap.append(item)
        self.currentsize +=1
        print(self.currentsize, 'Size')
        self.move(self.currentsize)
        
    
    def getheap(self):
        return self.Heap
        
    
b = BinHeap()
b.insert(1)
b.insert(11)
b.insert(10)
print(b.getheap())
