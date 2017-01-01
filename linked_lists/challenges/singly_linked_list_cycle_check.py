"""
Given a singly linked list, write a function which takes in the first node 
in a singly linked list and returns a boolean indicating if the linked list 
contains a "cycle".
A cycle is when a node's next point actually points back to a previous node 
in the list. This is also sometimes known as a circularly linked list.
You've been given the Linked List Node class code:
"""

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        
def cycle_check(node):
    m1 = m2 = node
    
    while m2 != None and m2.nextnode != None:
        m1 = m1.nextnode
        m2 = m2.nextnode.nextnode
        if m1 == m2:
            return True
            
    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert_equal(sol(a),True)
        assert_equal(sol(x),False)
        
        print "ALL TEST CASES PASSED"
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)