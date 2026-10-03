class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        
        longest = 0
        for n in nums:
            if n - 1 in s:
                continue
            run = 1
            while n + run in s:
                run += 1
            longest = max(longest, run)
        return longest