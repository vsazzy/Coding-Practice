def occurence(lst):
    dic={}
    for i in lst:
        if lst[i] in dic:
            dic[lst[i]]+=1
        else:
            dic[lst[i]]=1
    for x in dic:
        print(x,dic[x])
    return dic
print(occurence([1,2,3,4,1,2]))