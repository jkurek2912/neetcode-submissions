class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == 0 - nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < 0 - nums[i]:
                    l += 1
                else:
                    r -= 1
            i += 1

        return res
