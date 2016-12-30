class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
        
    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)