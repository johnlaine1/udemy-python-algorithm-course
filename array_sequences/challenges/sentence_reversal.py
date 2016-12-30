"""
Given a string of words, reverse all the words. For example:
Given:
'This is the best'

Return:
'best the is This'

As part of this exercise you should remove all leading and trailing 
whitespace. So that inputs such as:
'  space here'  and 'space here      '

both become:
'here space'
"""
def reverse_arr(arr):
    """Reverses elements in an array.
    
    Implemented instead of using built in 'reversed()'
    """
    s_len = len(arr)
    s_len_mid = (s_len / 2) if (s_len % 2 == 0) else ((s_len - 1) / 2)
    
    for a in xrange(s_len_mid):
        b = (s_len - 1) - a
        arr[a], arr[b] = arr[b], arr[a]
    return arr

def convert_to_arr(s):
    """Converts the words in a string to an array
    
    Implemented instead of using built in strip() and split().
    """
    words = []
    length = len(s)
    i = 0
    
    while i < length:
        if s[i] != ' ':
            word_start = i
            while i < length and s[i] != ' ':
                i += 1
            words.append(s[word_start:i])
        i += 1
    return words

def rev_word(s):
    return ' '.join(reverse_arr(convert_to_arr(s)))


    
# print rev_word('how now brown cow')

##########################################


    
    
    
    
"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print "ALL TEST CASES PASSED"
        
# Run and test
t = ReversalTest()
t.test(rev_word)

    