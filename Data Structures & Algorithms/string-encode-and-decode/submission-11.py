class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        c = 0
        while c < len(s):
            j = c
            while s[j] != "#":
                j += 1
            l = int(s[c : j])
            res.append(s[j + 1 : j + 1 + l])
            c = j + l + 1
        return res