class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9):
            valid_row = set()
            for x in range(9):
                cell = board[x][y]

                if cell == '.':
                    continue
                
                if cell in valid_row:
                    return False

                valid_row.add(cell)
         
        for y in range(9):
            valid_col = set()
            for x in range(9):
                cell = board[y][x]

                if cell == '.':
                    continue
                
                if cell in valid_col:
                    return False

                valid_col.add(cell)

        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                valid_sqr = set()

                for i in range(y, y+3):
                    for j in range(x, x+3):
                        cell = board[i][j]

                        if cell == '.':
                            continue
                        
                        if cell in valid_sqr:
                            return False
                        
                        valid_sqr.add(cell)
        
        return True

        