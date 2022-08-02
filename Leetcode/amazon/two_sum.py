def TwoSum(nums, target):
    seen = {}

    for idx, num in enumerate(nums):
        if target - num in seen:
            print(seen)
            return [idx, seen[target-num]]
        seen[num] = idx

print(TwoSum( [-3,4,3,90], 0))


