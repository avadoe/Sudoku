def empty_cell(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 0:
                return row, col
            
    return None

def is_valid_move(grid, num, row, col):
    for c in range(len(grid)):
        if grid[row][c] == num:
            return False
        
    for r in range(len(grid)):
        if grid[r][col] == num:
            return False
        
    box_start_row, box_start_col = row - (row % 3), col - (col % 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if grid[i][j] == num:
                return False
            
    return True

def sudoku_solver(grid):
    vacant = empty_cell(grid)
    if not vacant: return True
    
    row, col = vacant
    
    for num in range(1, 10):
        if is_valid_move(grid=grid, row=row, col=col, num=num):
            grid[row][col] = num
            if sudoku_solver(grid=grid):
                return True
            
            grid[row][col] = 0
            
    return False