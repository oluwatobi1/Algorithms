class Stack(object):
    """
    This uses a LIFO structure Ordering principle.
    Taking advantage of python lists

    Stack():  initializes an empty stack. Takes no parameters and returns an empty stack
    push(item): pushes a single item to the top of the stack. Takes the item and returns nothing
    pop(): removes the item at the top of stack. It takes no parameter and the item. The stack is modified
    Peek(): Returns the item on the top of the stack. It needs no parameter. The stack is not modified.
    isempty(): Returns a boolean value if the stack is empty.
    size():Returns the number of items in the stack.
    view(); Returns all items in the stack.
    
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def isempty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)
    def view(self):
        return self.stack


    