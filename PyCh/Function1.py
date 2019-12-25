##def add(x,y):
##    c=x+y
#    d=x-y
#    return c,d
#result1,result2=add(5,9999)
#print(result1,result2)

def update(a):
    print(id(a))
    a[1]=9
    print(id(a))
    print("x", a)
a=[1,10,20]

print(id(a))
update(a)
print("a", a)