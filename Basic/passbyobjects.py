#so python passes everything by object not necessary by value or reference
#for ex it uses pass by value for immutable objects and ref for mutable ones

#pass by value

def value(x):
    x=x+3
    print(x)

a=3
value(a)
print('outside function',a)

#pass by reference
def reference(x):
    x.append(4)
    print(x)

a=[1,2,3]
reference(a)
print('outside function',a)