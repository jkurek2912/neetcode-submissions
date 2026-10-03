class Solution:
    def can(self, piles, h, speed) -> bool:
        time = 0
        for p in piles:
            time += math.ceil(p / speed)
        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            speed = l + (r - l) // 2
            if self.can(piles, h, speed):
                r = speed
            else:
                l = speed + 1
        
        return l
    