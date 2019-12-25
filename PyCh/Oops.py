class Computer:
    def config(self):
        print("1Ib,i5,16Gb")
x = 9
print(type(x))
a = '8'
print(type(a))
com1=Computer()
print(type(com1))
Computer.config(com1)
com1.config()

"""class Computer:

    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()


Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()"""