class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        m = -1
        while t <= b:
            m = t + (b - t) // 2
            if matrix[m][l] == target or matrix[m][r] == target:
                return True
            if matrix[m][l] < target and matrix[m][r] > target:
                break
            if matrix[m][l] > target:
                b = m - 1
            else:
                t = m + 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[m][mid] == target:
                return True
            if matrix[m][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

                