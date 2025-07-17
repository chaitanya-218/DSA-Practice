def find_max(val):
    if not val:
        return None
    
    max_num=val[0]
    for x in val:
        if x>max_num:
            max_num=x

    return max_num

p1=[1,2,3,4,5,66]
print(find_max(p1))