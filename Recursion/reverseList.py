def rev(lst,start,end):
    if start<end:
        lst[start], lst[end]=lst[end],lst[start]
        rev(lst,start+1, end-1)
    return lst

print(rev([1,2,3,4],0,3))
