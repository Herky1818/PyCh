from functools import reduce
"""def is_even(n):
    return n%2==0
    return n%2==1"""
#def update(n):
 #   return n+1
nums=[1,233,2,3,11,4,5,6,7,9,8]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
print(list(map(lambda n:n+1,evens)))
print(reduce(lambda a,b:a+b,nums))