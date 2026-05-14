class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Needs Valid Row
        # Needs Valid Column
        # Needs Valid Grid

        for y, col in enumerate(board):
            unique_col = set()
            print(col)
            
            for x, row in enumerate(col):
                cell = board[x][y]

                if cell == ".":
                    continue

                if cell in unique_col:
                    print("Failed Column check")
                    print(cell)
                    return False
                
                unique_col.add(cell)
        
        for x, row in enumerate(board):
            unique_row = set()
            
            for y, col in enumerate(row):
                cell = board[x][y]

                if cell == ".":
                    continue

                if cell in unique_row:
                    print("Failed Row Check")
                    return False
                
                unique_row.add(cell)
        
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                unique_grid = set()

                for k in range(i, i+3):
                    for l in range(j, j+3):
                        cell = board[k][l]

                        if cell == ".":
                            continue

                        if cell == "5":
                            print(f"{i} {j}")
                        if cell in unique_grid:
                            print("Failed grid check")
                            return False
                        
                        unique_grid.add(cell)
        
        return True
        
        


        
        