class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set()
        for n in nums:
            m.add(n)
        
        longestConsecutive = 0
        for n in nums:
            if n - 1 in m:
                continue
            
            run = 1
            while n + run in m:
                run += 1
            
            longestConsecutive = max(longestConsecutive, run)
        
        return longestConsecutive