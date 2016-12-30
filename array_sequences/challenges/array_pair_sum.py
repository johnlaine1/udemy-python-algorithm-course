"""
Given an integer array, output all the unique pairs that sum up to a 
specific value k.
So the input:
pair_sum([1,3,2,2],4)

would return 2 pairs:
 (1,3)
 (2,2)
"""

def pair_sum(arr, k):
    pairs = []
    arr_len = len(arr)
    for n in xrange(arr_len - 1):
        for n1 in xrange(n+1, arr_len):
            if arr[n] + arr[n1] == k:
                if (not (arr[n], arr[n1]) in pairs and
                    not (arr[n1], arr[n]) in pairs):
                    pairs.append((arr[n], arr[n1]))
                
    return len(pairs)
    
# print pair_sum([1,3,2,2],4)


def pair_sum2(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #print '\n'.join(map(str,list(output)))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print 'ALL TEST CASES PASSED'
        
#Run tests
t = TestPair()
t.test(pair_sum2)