class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            unique_row = set()
            for y in range(9):
                cell = board[x][y]
                if cell == ".":
                    continue

                if cell in unique_row:
                    return False
                
                unique_row.add(cell)
        
        for x in range(9):
            unique_col = set()
            for y in range(9):
                cell = board[y][x]
                if cell == ".":
                    continue

                if cell in unique_col:
                    return False
                
                unique_col.add(cell)
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                unique_grid = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        cell = board[k][l]
                        if cell == ".":
                            continue
                        
                        if cell in unique_grid:
                            return False
                        
                        unique_grid.add(cell)
        
        return True