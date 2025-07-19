def moving_negative(val):
    if not val:
        return None
    
    start=0
    end=len(val)-1

    while start<end:
        if val[start]<0:
            start+=1
        elif val[end]>0:
            end-=1
        else:
            val[start],val[end]=val[end],val[start]

            start += 1
            end -= 1  # Move both pointers after swap
    
    return val


P1=[-1,3,4,-3,6,-7,-8,0,9]
print("After moving negatives:", moving_negative(P1))