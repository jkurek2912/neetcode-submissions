class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            if c == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                else:
                    return False
            if c == '}':
                if stk and stk[-1] == '{':
                    stk.pop()
                else:
                    return False
            if c == ']':
                if stk and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
        return not stk