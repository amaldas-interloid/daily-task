                      #bubble sort...............................................




nums = [10,2,34,56,1,77,3]
n = len(nums)
for i in range(n):
    for j in range(0,n-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] =nums[j+1],nums[j]
print(nums[4]) 