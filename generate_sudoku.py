from dokusan import generators
import numpy as np
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

def generate_sudoku_dokusan():
    arr = generators.random_sudoku()
    arr = np.array(list(str(arr)))
    arr = arr.reshape((9, 9))

    arr = [[int(x) for x in row] for row in arr]

    return arr

random_sudoku = generate_sudoku_dokusan()
for row in random_sudoku: print(row)
print()
x = algo.sudoku_solver(random_sudoku)
for row in random_sudoku: print(row)