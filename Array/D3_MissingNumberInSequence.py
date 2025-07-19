# Problem: Find the missing number in a sequence from 1 to n.
# Thought process:
# - We know the sum of first n numbers = n*(n+1)//2
# - So if we calculate the actual sum of the array, the missing number will be:
#   missing = expected_sum - actual_sum
# Why this approach:
# - No sorting or extra space needed
# - Fast and clean O(n) time and O(1) space


def find_missing(val):
    # Edge case: return None if list is empty
    if not val:
        return None

    # Total number of elements should be len(val) + 1 since one number is missing
    n = len(val) + 1

    # Calculate sum of first n natural numbers using formula
    sum_n_natural_nums = (n * (n + 1)) // 2

    # Calculate actual sum of elements in the given array
    sum_of_val = sum(val)

    # The missing number will be the difference between expected and actual sum
    missing_element = sum_n_natural_nums - sum_of_val

    # Print the result
    print(f"The missing element from the array {val} is {missing_element}")


P1=[2,3,4,6,7,5,9,8]
find_missing(P1)
