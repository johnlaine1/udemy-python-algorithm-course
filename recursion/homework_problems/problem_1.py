def rec_sum(n):
    if n == 1:
        return 1
        
    return n + rec_sum(n-1)
    
print rec_sum(int(raw_input('Please enter a number: ')))