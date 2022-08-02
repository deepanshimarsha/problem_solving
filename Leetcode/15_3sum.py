#category - Algorithm
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(0, len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r = r - 1
                elif total < 0:
                    l = l + 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l = l + 1
                    while l < r and nums[r] == nums[r - 1]:
                        r = r - 1

                    l = l + 1
                    r = r - 1
        return res