def sort(nums):
    for i in range(len(nums)):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]#Harsha How R You
        nums[i]=nums[minpos]
        nums[minpos]=temp
        print(nums)
nums=[5,3,8,6,7,2,56,2]
sort(nums)
print(nums)