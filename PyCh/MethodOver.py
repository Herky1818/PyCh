class A:
    def show(self):
        print("In A show")
class B(A):
    def show(self):
    #pass
        print("In B Show")
a1=B()
a1.show()