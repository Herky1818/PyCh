pos=-1
def search(list,n):
    i=0
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True

    return False
"""
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False
"""
list=[5,68,7,9,34,42]
n=9
if search(list,n):
    print("Found at: ", pos+1)
else:
    print("Not Found")