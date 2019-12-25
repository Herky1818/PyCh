class Student:
    def __init__(self,m,m1):
        self.m=m
        self.m1=m1
    def __add__(self, other):
        m=self.m+other.m
        m1=self.m1+other.m1
        s2=Student(m,m1)
        return s2
    def __gt__(self, other):
        r=self.m+self.m
        r1=other.m1+other.m1
        if r>r1:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format( self.m,self.m1)
s=Student(23,46)
s1=Student(32,47)
s2=s + s1
if s>s1:
    print("S wins")
else:
    print("s1 wins")
print(s2.m)
print(s2.m)
a=9
print(a.__str__())
print(s1)
print(s)







#a='5'
#b='6'
#print(a+b)
#print(str.__add__(a,b))
