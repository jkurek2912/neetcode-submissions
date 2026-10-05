class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                square = set()
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if board[i + a][j + b] != "." and board[i + a][j + b] in square:
                            return False
                        square.add(board[i + a][j + b])
        
        for i in range(0, 9):
            row = set()
            col = set()
            for j in range(0, 9):
                if board[i][j] != "." and board[i][j] in row:
                    return False
                if board[j][i] != "." and board[j][i] in col:
                    return False
                row.add(board[i][j])
                col.add(board[j][i])

        return True
