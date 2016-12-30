import sys

lst = [1,2,3,4,5,6,7,8,9,10]

def comp(lst):
    print lst[0] # O(1)
    mid = len(lst)/2
    for item in lst[:mid]: # O(n/2)
        print item
        
    for x in xrange(10): # O(10)
        print "Hello World"
        
def is_match(lst, match):
    for item in lst:
        if item == match:
            return True
    return False
    
# print is_match(lst, 1) # O(1)
# print is_match(lst, 11) # O(n)

def printer(n=10):
    for x in xrange(n):
        print "Hello"
        
# printer(1)

def create_list(n):
    new_list = []
    for i in xrange(n):
        new_list.append("Word")
    return new_list
    
# print create_list(25)

class Child(object):
    def __init__(self, name):
        self.name = name
        
    def play(self):
        print '{} is playing...'.format(self.name)
        

def ref_arr():
    isabel = Child('isabel')
    sophia = Child('sophia')
    arr1 = [sophia] * 5
    arr2 = [isabel] * 5
    
    arr1.extend(arr2)
    arr2[0].name = 'Isabel'
    print arr1
    for child in arr1:
        child.play()
        print sys.getsizeof(child)
    
# ref_arr()


