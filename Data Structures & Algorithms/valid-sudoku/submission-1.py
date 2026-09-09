class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowChecker = defaultdict(set)
        colChecker = defaultdict(set)
        squareChecker = defaultdict(set)

        # rows
        for i in range(9):
            for j in range(9): # cols
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in rowChecker[i]:
                        return False
                    if board[i][j] in colChecker[j]:
                        return False
                    if board[i][j] in squareChecker[(i // 3, j // 3)]:
                        return False
                    rowChecker[i].add(board[i][j])
                    colChecker[j].add(board[i][j])
                    squareChecker[(i // 3, j // 3)].add(board[i][j])
        return True