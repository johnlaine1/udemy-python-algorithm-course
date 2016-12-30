"""
String Compression
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 
'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of 
single or double letters. For instance, it is okay for 'AAB' to return 
'A2B1' even though this technically takes more space.
The function should also be case sensitive, so that a string 'AAAaaa' 
returns 'A3a3'.
"""

def compress(s):
    s_length = len(s)
    
    if s_length == 0:
        return ''
    if s_length == 1:
        return '{}1'.format(s)
        
    counter = 1
    previous = s[0]
    result = ''
    
    for current in s[1:]:
        if current == previous:
            counter += 1
        else:
            result = '{}{}{}'.format(result, previous, counter)
            counter = 1
        previous = current
    result = '{}{}{}'.format(result, previous, counter)
    return result




if __name__ == '__main__':
    """
    RUN THIS CELL TO TEST YOUR SOLUTION
    """
    from nose.tools import assert_equal
    
    class TestCompress(object):
    
        def test(self, sol):
            assert_equal(sol(''), '')
            assert_equal(sol('AABBCC'), 'A2B2C2')
            assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
            print 'ALL TEST CASES PASSED'
    
    # Run Tests
    t = TestCompress()
    t.test(compress)