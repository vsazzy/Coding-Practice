def pal(s,start,end):
    if start>=end:
        return 1
    if s[start]!=s[end]:
        return 0
    return pal(s,start+1,end-1)

ss="sbcdcbs"
print(pal(ss,0,len(ss)-1))

