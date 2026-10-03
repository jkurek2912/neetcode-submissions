class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for s in tokens:
            if s not in "+-/*":
                stk.append(int(s))
            else:
                a = int(stk[-1])
                stk.pop()
                b = int(stk[-1])
                stk.pop()
                if s == "+":
                    stk.append(a + b)
                elif s == "-":
                    stk.append(b - a)
                elif s == "/":
                    stk.append(int(b / a))
                else:
                    stk.append(a * b)
        return stk[-1]