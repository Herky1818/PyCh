a=10
b=10
c=11
print(id(a))
def something():

    a=9
    x=globals()['a']
    print(id(x))
    print('in',a)

    globals()['a']=15
something()
print('out',a)