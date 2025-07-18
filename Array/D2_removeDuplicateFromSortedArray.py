
# ✅ Problem: Remove duplicates from a sorted array in-place.
# 🔧 Constraints: Must use O(1) extra space (modify in-place).
# 🎯 Strategy:
#     - Use two-pointer technique.
#     - Pointer 'j' tracks the last unique value found.
#     - Pointer 'i' scans from left to right.
#     - When val[i] != val[j], we found a new unique element.
#     - Move val[i] to val[j+1] and increment j.
# 🚀 Final Result:
#     - The first j+1 elements in the array are the unique elements.
#     - We return val[:j+1] to return only the meaningful portion.

def removeDuplicate(val):
    if not val:
        return None
    
    j = 0
    for i in range(1, len(val)):
        if val[i] != val[j]:
            j += 1
            val[j] = val[i]

    return val[:j+1]


P1 = [1,1,1,2,3,3,3,3,4,4,5,5,5,6,7,8,9,9,9]
print(f"The array after removing duplicates is: {removeDuplicate(P1)}")
