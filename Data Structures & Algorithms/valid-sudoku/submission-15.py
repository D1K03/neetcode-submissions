class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = defaultdict(set)
        seen_col = defaultdict(set)
        seen_sqr = defaultdict(set)
        

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell == '.':
                    continue
                
                if (cell in seen_row[r] or cell in seen_col[c] or cell in seen_sqr[(r // 3, c // 3)]):
                    return False

                seen_row[r].add(cell)
                seen_col[c].add(cell)
                seen_sqr[(r // 3, c // 3)].add(cell)
        
        return True