class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        if nums[pivot] == target:
            return pivot
        
        l, r = 0, len(nums) - 1
        if pivot > 0 and target >= nums[0]:
            r = pivot - 1
        else:
            l = pivot
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1