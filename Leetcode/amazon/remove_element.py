

def remove_element(nums,val):
    i, j = 0, len(nums) - 1
    
    while i <= j:
        if nums[i] == val:
            if nums[j] != nums[i]:
                nums[i],nums[j]= nums[j],nums[i]
                i = i + 1
            else:
                j = j - 1
        else:
            i = i + 1

            
    return i,nums

print(remove_element([3,3],5))

