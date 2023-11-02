def reorder_students(L):
    '''
        Input: L | linked list with head L.head and size L.size
        Output: None |
        This function should modify list L to reverse its last half.
        Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    '''
    
    h = L.head
    for _ in range(n):
        h = h.next
   
    prev, cur = None, h
    while cur is not None:
        n = cur.next
        cur.next = prev
        prev = cur
        cur = n

    h.next = prev

    return h