
class Stack(object):
    """Implementation of a basic stack"""
    
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def isEmpty(self):
        return len(self.items) == 0
        
    def size(self):
        return len(self.items)
        
        
def balance_check(s):
    
    # Edge case check, if number of items is not even, it can't be balanced.
    if len(s) % 2 != 0:
        return False
        
    stack = Stack()
    open_p = ['(', '[', '{']
    close_p = [')', ']', '}']
    
    for p in s:
        if p in open_p:
            stack.push(open_p.index(p))
        elif close_p.index(p) != stack.pop():
            return False
    
    return stack.isEmpty()


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        assert_equal(sol('('),False)
        print 'ALL TEST CASES PASSED'
        
# Run Tests

t = TestBalanceCheck()
t.test(balance_check)