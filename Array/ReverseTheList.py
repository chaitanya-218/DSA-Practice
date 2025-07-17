def reverse_lst(val):
    start=0
    end=len(val)-1

    while start<end:
        val[start],val[end]=val[end],val[start]

        start+=1
        end-=1

    return val

L1=[1,2,1,2,1,2]
print(reverse_lst(L1))