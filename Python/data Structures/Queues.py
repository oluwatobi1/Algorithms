class Queue(object):
    """
    This follows the FIFO structure
    Leverages the python lists

    Queue(): creates an empty queue. Accepts no parameter and returns an empty queue.
    enqueue(item): adds a new item to the rear of the queue. accepts the item and returns nothing.
    dequeue(): remove items from the front of the queue. accepts nothing and return the item. The queue is modified.
    size(): Returns the number of items in the queue. needs no parameter and returns and integer.
    """

    def __init__(self):
        self.que = []

    def enqueue(self, item):
        self.que.insert(0, item)

    def dequeue(self):
        return self.que.pop()
    def size(self):
        return len(self.que)

    def view(self):
        return self.que













    #old (different code approach)
    
    # def __init__(self):
    #     self.que = []
    #     self.head = None
    # def enqueue(self, element):
    #     if not self.head:
    #         self.head = element
    #     self.que.append(element)
    # def dequeue(self):
    #     if self.que != []:
    #         var = self.que.pop(0)            
    #         self.head = self.que[0] if len(self.que)>=1 else None
    #         return var
    #     else:
    #         self.head = None
    #         raise AssertionError('Queue is empty')



