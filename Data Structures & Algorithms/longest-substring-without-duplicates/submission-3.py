class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = set()
        l, r = 0, 0
        maxLength = 0
        while r < len(s):
            if s[r] not in table:
                table.add(s[r])
                maxLength = max(maxLength, r - l + 1)
            else:
                while s[l] != s[r]:
                    table.discard(s[l])
                    l += 1
                l += 1
            r += 1
        return maxLength
