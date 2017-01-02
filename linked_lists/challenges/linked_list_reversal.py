class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
def reverse(head):
    n1 = head
    n2 = n1.nextnode
    n3 = n2.nextnode
    
    n1.nextnode = None
    
    while n2 != None:
        n2.nextnode = n1
        n1 = n2
        n2 = n3
        if n3:
            n3 = n3.nextnode
    return n1
    
##### Another version #####    
    
def reverse2(head):
    previous_node = head
    current_node = None
    next_node = None
    
    while current_node:
        next_node = current_node.nextnode
        current_node.nextnode = previous_node
        
        previous_node = current_node
        current_node = next_node
        
    return previous_node
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.nextnode = b
b.nextnode = c
c.nextnode = d

print a.nextnode.value
print b.nextnode.value
print c.nextnode.value

reverse(a)

print d.nextnode.value
print c.nextnode.value
print b.nextnode.value