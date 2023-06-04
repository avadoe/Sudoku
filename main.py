import pygame
import math
import generate_sudoku, algo

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CHARCOALGRAY = (51, 51, 51)

WIDTH = 630
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Sudoku Solver')
clock = pygame.time.Clock()

ROWS = 9
CELLSIZE = WIDTH // ROWS

sudoku = generate_sudoku.generate_sudoku_dokusan()

def draw():
    WINDOW.fill(WHITE)
    for i in range(ROWS + 1):
        if i % 3 == 0: line_color = CHARCOALGRAY
        else: line_color = BLACK
        if i % 3 != 0:
            pygame.draw.line(WINDOW, line_color, (0, i * CELLSIZE), (WIDTH, i * CELLSIZE), 2)
            pygame.draw.line(WINDOW, line_color, (i * CELLSIZE, 0), (i * CELLSIZE, WIDTH), 2)
        else:
            pygame.draw.line(WINDOW, line_color, (0, i * CELLSIZE), (WIDTH, i * CELLSIZE), 4)
            pygame.draw.line(WINDOW, line_color, (i * CELLSIZE, 0), (i * CELLSIZE, WIDTH), 4)
        
    font = pygame.font.Font(None, 40)
    for row in range(ROWS):
        for col in range(ROWS):
            number = sudoku[row][col]
            
            if number != 0:
                num_text = font.render(str(number), True, BLACK)
                num_rect = num_text.get_rect(center=(col * CELLSIZE + CELLSIZE//2, row * CELLSIZE + CELLSIZE/2))
                WINDOW.blit(num_text, num_rect)


running = True
solve = False

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve = True
                
    if solve:
        algo.sudoku_solver(sudoku)
        solve = False
            
    draw()
        
    pygame.display.update()
    pygame.time.delay(1000)
        
pygame.quit()   