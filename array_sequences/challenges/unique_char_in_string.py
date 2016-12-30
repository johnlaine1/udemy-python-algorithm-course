"""
Problem
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should 
return True. The string 'aabcde' contains duplicate characters and should 
return false.
"""

def uni_char(s):
    unique = set()
    
    for c in s:
        if c in unique:
            return False
        else:
            unique.add(c)
    return True
    

# Another approach using Python's built in function
def uni_char2(s):
    return len(set(s)) == len(s)


##### TESTS #####
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'
        
# Run Tests
t = TestUnique()
t.test(uni_char)