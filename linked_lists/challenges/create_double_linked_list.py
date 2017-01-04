class Node(object):
    def __init__(self, value):
        self.value = value
        self.previous_node = None
        self.next_node = None
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next_node = b
b.previous_node = a
b.next_node = c
c.previous_node = b
c.next_node = d
d.previous_node = c