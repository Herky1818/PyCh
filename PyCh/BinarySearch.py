pos=-1
def search(list,n):
    l=0
    u=len(list)
    #while l<=u:
    for l in range(u):
        mid= (l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if l<u:
                l=mid+1
            else:
                u=mid-1
    return False

list=[5,68,7,9,34,42]
n=9
if search(list,n):
    print("Found at: ",pos+1)
else:
    print("Not Found")