# # Input: n = 4

# # Output: "1211"

# # Explanation:

# # countAndSay(1) = "1"
# # countAndSay(2) = RLE of "1" = "11"
# # countAndSay(3) = RLE of "11" = "21"
# # countAndSay(4) = RLE of "21" = "1211"


def countAndSay( n):
    if n == 1:
        return "1"
    return count(countAndSay(n - 1))
    
def count(s):
    c = s[0]
    count = 1
    res = ""
    for char in s[1: ]:
        if char == c:
            count += 1
        else:
            res  = res + str(count) + c
            c = char
            count = 1
    res = res + str(count) + c
    return res

print(countAndSay(4))



def say(n):
    if n==1:
        return "1"
    return counts(say(n-1))

def counts(s):
    res=""
    c=s[0]
    count=1
    for i in s[1:]:
        if i==c:
            count+=1
        else:
            res=res+str(count)+c
            c=i
            count=1
    res=res+str(count)+c
    return res
print(say(4))