def MoveTheZero(val):
    """
    Moves all 0's in the list to the end while keeping the order of non-zero elements.
    
    Approach:
    - Two pointer method: one pointer (i) scans the array, the other (last_nonzero_index)
      tracks where the next non-zero should go.
    - When a non-zero is found, we swap it with the element at last_nonzero_index.
    - This pushes all zeroes to the right without using extra space.
    """
    
    # Edge case: return None if the input list is empty
    if not val:
        return None

    # This pointer keeps track of where the next non-zero element should go
    last_nonzero_index = 0

    # Traverse through the list
    for i in range(len(val)):
        if val[i] != 0:
            # Swap current element with the element at last_nonzero_index
            val[i], val[last_nonzero_index] = val[last_nonzero_index], val[i]
            # Move the pointer to next position
            last_nonzero_index += 1

    return val

# Input list
P1 = [1, 0, 3, 4, 5, 0, 7, 8]

# Output: [1, 3, 4, 5, 7, 8, 0, 0]
print("After moving zeroes:", MoveTheZero(P1))
