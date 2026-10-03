class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            while i > 0 and i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == 0 - nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] > 0 - nums[i]:
                    r -= 1
                else:
                    l += 1
            i += 1
        return res
