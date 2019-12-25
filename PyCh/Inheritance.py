class A:
    def __init__(self):
        print("In A init")
    def f1(self):
        print("1st")
    def f2(self):
        print("2nd")
class B:
    def __init__(self):
        super().__init__()
        print("In B init")
    def f3(self):
        print("3rd")
    def f4(self):
        print("4th")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")
    def f5(self):
        print("3rd")
    def f6(self):
        print("4th")


#a1=A()
a1=C()
#a1.__init__()
a1.f1()
a1.f5()
b1=B()
b1.f6