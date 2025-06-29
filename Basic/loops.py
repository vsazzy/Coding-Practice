#normal loop
for i in [1,2,3]:
    print(i)
print("*********")
#with range
for i in range(4):
    print(i)

print("*********")

for index, num in enumerate(['a','b','c']):
    print(index,num)

print("*********")

a=[1,2,3]
b=["a","b","c"]
for index,num in zip(a,b):
    print(index,num)

print("*********")

x=0
while x<5:
    print(x)
    x+=1
print("*********")

print([i**2 for i in range(3)])
print({i:i**2 for i in range(3)})

print(list(map(lambda x: x*2, [1,2,3])))
print(list(filter(lambda x: x%2==0, range(5))))