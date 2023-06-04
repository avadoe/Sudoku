import sys
sys.setrecursionlimit(10**6)
import algo
import random

def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]
    algo.sudoku_solver(grid=grid)
    
    vacant_cells = 0
    
    while vacant_cells != 40:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        
        if grid[row][col] != 0:
            grid[row][col] = 0
            vacant_cells += 1   
    
    return grid

random_sudoku = generate_sudoku()
for row in random_sudoku: print(row)
print()
x = algo.sudoku_solver(random_sudoku)
for row in random_sudoku: print(row)