def find_second_max(val):
    # Edge case: if the list is empty, return None
    if not val:
        return None

    # Initialize first_max and second_max to the lowest possible number
    first_max = second_max = float('-inf')

    # Traverse the list to find the top two unique max numbers
    for x in val:
        if x > first_max:
            # If x is greater than current max, update both
            second_max = first_max
            first_max = x
        elif x < first_max and x > second_max:
            # If x is less than first_max but greater than second_max, update second_max
            second_max = x

    return second_max

# My input list
P1 = [3, 4, 6, 7, 2, 1]

# Output: 6
print("Second largest:", find_second_max(P1))
