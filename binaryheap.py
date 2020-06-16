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
        return self.Heap
        
    
    
    def delMin(self):
        temp = self.Heap[1]
        self.Heap[1] = self.Heap[self.currentsize]        
        self.Heap.pop()
        self.currentsize-=1
        self.arrange(1)
        
    def arrange(self, index):
        while index*2< self.currentsize:
            mc = self.minchild(index)
            
            if self.Heap[index]>self.Heap[mc]:
                temp = self.Heap[index]
                self.Heap[index] = self.Heap[mc]
                self.Heap[mc] =temp
                
            index = mc

    def minchild(self, indx):
        if indx*2+1>self.currentsize:
            return indx*2
        else:
            if self.Heap[indx*2]>self.Heap[indx*2+1]:
                return indx*2+1
            else:
                return indx*2
        
    def getheap(self):
        return self.Heap
            
            
b = BinHeap()
b.insert(1)
b.insert(11)
b.insert(10)
print(b.getheap())
