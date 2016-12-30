"""
Problem
Given two strings, check to see if they are anagrams. An anagram is when 
the two strings can be written using the exact same letters 
(so you can just rearrange the letters to get a different phrase or word).
For example:
"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" 
and "dog" and "o d g".
"""

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)
        
# This is the preferred solution
def anagram2(s1, s2):
    # Clean up the strings
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge case check
    if len(s1) != len(s2):
        return False
        
    count = {}
    
    for l in s1:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1
    
    for l in s2:
        if l in count:
            count[l] -= 1
        else:
            count[l] = 1
            
    for i in count:
        if not count[i] != 0:
            return False
            
    return True
    
    
        
        
    
if __name__ == '__main__':

    from nose.tools import assert_equal
    
    class AnagramTest(object):
        
        def test(self,sol):
            assert_equal(sol('go go go','gggooo'),True)
            assert_equal(sol('abc','cba'),True)
            assert_equal(sol('hi man','hi     man'),True)
            assert_equal(sol('aabbcc','aabbc'),False)
            assert_equal(sol('123','1 2'),False)
            print "ALL TEST CASES PASSED"
    
    # Run Tests
    t = AnagramTest()
    t.test(anagram2)