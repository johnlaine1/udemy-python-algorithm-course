class Queue2Stacks(object):
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        
    def enqueue(self, item):
        self.in_stack.append(item)
        
    def dequeue(self):
        # Make sure the outstack is empty first before adding more items.
        if not self.out_stack:
            
            # If the outstack is empty, append all the items from in_stack
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
                
        return self.out_stack.pop()


"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in xrange(5):
    q.enqueue(i)
    
for i in xrange(5):
    print q.dequeue()