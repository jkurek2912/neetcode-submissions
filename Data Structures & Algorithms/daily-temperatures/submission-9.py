class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            tup = [temperatures[i], i]
            if not stk:
                stk.append(tup)
            elif tup[0] < stk[-1][0]:
                res[i] = stk[-1][1] - tup[1]
                stk.append(tup)
            else:
                while stk and stk[-1][0] <= tup[0]:
                    stk.pop()
                if stk:
                    res[i] = stk[-1][1] - tup[1]
                stk.append(tup)
        return res
