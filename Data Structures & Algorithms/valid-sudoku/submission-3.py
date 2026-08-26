class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        cols: dict(set) = defaultdict(set)
        rows: dict(set) = defaultdict(set)
        box: dict(set) = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in cols[col]:
                        return False
                    if board[row][col] in rows[row]:
                        return False
                    if board[row][col] in box[(row // 3, col // 3)]:
                        return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                box[(row // 3, col // 3)].add(board[row][col])
    
        return True