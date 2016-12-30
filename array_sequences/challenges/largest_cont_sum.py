""" Given an array of integers (positive and negative) 
find the largest continuous sum.
"""

def large_cont_sum(arr):
    arr_len = len(arr)
    largest = [arr[0], None, None]
    
    for n1 in xrange(arr_len):
        if arr[n1] > largest[0]:
            largest[0] = arr[n1]
            largest[1] = n1
            largest[2] = n1 + 1
        for n2 in xrange(n1, arr_len):
            total = sum(arr[n1:n2])
            if total > largest[0]:
                largest[0] = total
                largest[1] = n1
                largest[2] = n2
                
    print 'Largest sum: {}, from sub array: {}'.format(largest[0], arr[largest[1]:largest[2]])
    return largest[0]


def large_cont_sum2(arr):
    # Check to see if array is length 0
    if len(arr) == 0:
        return 0
        
    # Set the max and current sum to the first element value.
    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        # Set the current sum as the higher of the two.
        current_sum = max(current_sum + num, num)
        
        # Set max as the higher between the current_sum and max_sum
        max_sum = max(current_sum, max_sum)
        
    return max_sum
    
# large_cont_sum([-1,1])



from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        assert_equal(sol([1,2,-1,4,5]), 11)
        print 'ALL TEST CASES PASSED'
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum2)