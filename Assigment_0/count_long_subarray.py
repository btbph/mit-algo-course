def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    if len(A) == 0:
        return 0
    
    prev = -1
    max_length = current_length = 0
    count = 0


    for a in A:
        if a > prev:
            current_length += 1

            if current_length == max_length:
                count += 1
            elif current_length > max_length:
                count = 1
                max_length = current_length
        else:
            current_length = 1
            
        prev = a

    return count
