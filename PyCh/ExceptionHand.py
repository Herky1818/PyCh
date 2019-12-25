a=10
b=5
try:
    print(a/b)
    k=int(input("Enter Number"))
    print(k)
except ZeroDivisionError as e:
    print("you have divided by zero")
except ValueError as e:
    print(" Input is wrong")
except Exception as e:
    print("Something Wrong")
finally:
    print("Resource Closed")