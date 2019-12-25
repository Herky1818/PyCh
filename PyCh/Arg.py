#def person(name,age=18):
#    print(name)
#    print(age)

#person(age=28,name='Harsha')


def sum(a, *b):
    c=a
    for i in b:
        c=c+i
    print(c)
sum(2,3,4,5)