def removeduplicates(nums):
    k = 1
    j = 0
    for i in range(0,len(nums)):
        if j == len(nums)-1 or j == len(nums):
            return(k)
        j = j + 1
        while nums[j] == nums[i]:
            if j == len(nums)-1:
                return k
            j = j + 1
        nums[i+1] , nums[j] = nums[j] , nums[i+1]
        k = k + 1
            

print(removeduplicates([0,0,1,1,1,2,2,3,3,4]))



