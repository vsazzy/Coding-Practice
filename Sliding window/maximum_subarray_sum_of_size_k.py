print("hello sliding window")

a=[2,3,4,2,5,7,7]
k=3

def max_sum(a,k):
    start=0
    end=0
    s=0
    mx=0
    while end<len(a):
        s+=a[end]
        if end-start+1<k:
            end+=1
        elif end-start+1==k:
            mx=max(mx,s)
            s=s-a[start]
            start=start+1
            end=end+1
    
    return mx
print(max_sum(a,k))
