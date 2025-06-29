#LIST: Mutable, ordered, Allows duplicates

lst=[1,2,3,4,22,21,45]
print(len(lst))
lst.append(33)
print(lst)
lst.insert(2,9)
print(lst)


#TUPLE: Immutable, unordered, allows duplicates

tup=(1,2,4,3,2)
x=tup.count(2)
print(x)


#SET: Unordered, Unique elements

set={1,2,3,4,7,3,3,3}
set2={1,2,3,4}
print(set)
print(set.intersection(set2))
print(set)
set2.discard(3)
print(set2)

#DICT: key value pairs and unique keys

d={
    "a":1,
    "b":2,
    "c":3,
}
print(d)
print(d.get("a"))
d["d"]=4
print(d)
d.update({"a":5})
print(d)


#Collections ->counter
from collections import Counter
c=Counter("mississipisis")
print(c.elements)
print(c)

#Dequeue
from collections import deque

s=deque([1,2,3])
s.appendleft(2)
print(s)
