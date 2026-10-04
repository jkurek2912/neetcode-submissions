class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            t = "".join(sorted(s))
            if t in m:
                m[t].append(s)
            else:
                m[t] = [s]
        return list(m.values())
