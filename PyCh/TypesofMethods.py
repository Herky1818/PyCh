class Student():
    school='Telusko'#class variable
    def __init__(self,m1,m2,m3):
        self.m1=m1 #Instance Variables
        self.m2=m2
        self.m3=m3
    def avg(self): #Instance Methods
        return (self.m1+self.m2+self.m3)/3
    """def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value"""
    @classmethod #Class MEthods
    def getSchool(cls):
        return cls.school
    @staticmethod #Static Methods
    def info():
        print("im done today")
s1=Student(45,35,24)
s2=Student(24,26,38)
#s1.set_m1(99)
Student.info()
print(s1.avg())
print(s1.getSchool())


