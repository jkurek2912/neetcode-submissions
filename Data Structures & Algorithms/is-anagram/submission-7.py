class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        tMap = {}

        for c1, c2 in zip(s, t):
            if c1 in sMap:
                sMap[c1] += 1
            else:
                sMap[c1] = 1
            if c2 in tMap:
                tMap[c2] += 1
            else:
                tMap[c2] = 1
        
        return sMap == tMap
            