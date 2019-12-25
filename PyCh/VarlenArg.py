def person(name, **kwargs):
    print(name)
    print(kwargs)
    for i,j in kwargs.items():
        print(i,j)
person('Harsha', age=21, mobile=8309851213, address='Bang')