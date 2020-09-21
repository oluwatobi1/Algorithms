class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    
    def __init__(self):
        self.que = []
        self.head = None

    def enqueue(self, element):
        if not self.head:
            self.head = element
        self.que.append(element)


    def dequeue(self):
        if self.que != []:
            var = self.que.pop(0)            
            self.head = self.que[0] if len(self.que)>=1 else None
            return var
        else:
            self.head = None
            raise AssertionError('Queue is empty')

    def front(self):
        if self.que != []:
            return self.que[0]
        else:
            return None

    def count(self):
        return len(self.que)
    
    def veiw(self):
        return self.que


