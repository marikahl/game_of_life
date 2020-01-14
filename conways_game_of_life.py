#!/usr/bin/env python3
import time
import pygame

area_width = 500
area_height = 500
cell_size = 10

top_left_x = 0
top_left_y = 0

def new_white_cells(grid):
    new_grid = [[0 for w in range(50)] for x in range(50)]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            summ = 0
            if i != 0 and j != 0 and i < len(grid)-1 and j < len(grid[i])-1:
                summ = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + \
                    grid[i][j-1] + grid[i][j+1] + \
                    grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
            elif i == 0:
                if j == 0:
                    summ = grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
                elif j == len(grid[1])-1:
                    summ = grid[i][j-1] + grid[i+1][j-1] + grid[i+1][j]
                else:
                    summ = grid[i][j-1] + grid[i+1][j-1] + grid[i][j+1] + \
                    grid[i+1][j] + grid[i+1][j+1]

            elif i == len(grid)-1:
                if j == 0:
                    summ = grid[i][j+1] + grid[i-1][j] + grid[i-1][j+1]
                elif j == len(grid[i])-1:
                    summ = grid[i][j-1] + grid[i-1][j-1] + grid[i-1][j]
                else:
                    summ = grid[i][j-1] + grid[i-1][j-1] + \
                    grid[i-1][j] + grid[i-1][j+1] + grid[i][j+1]
            
            elif j == 0:
                summ = grid[i-1][j] + grid[i-1][j+1] + grid[i][j+1] + grid[i+1][j+1] + grid[i+1][j]  
            elif j == len(grid[i])-1:
                summ = grid[i-1][j] + grid[i-1][j-1] + grid[i][j-1] + grid[i+1][j-1] + grid[i+1][j]
            
            if grid[i][j]:
                if summ == 2 or summ == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
            else:
                if summ == 3:
                    new_grid[i][j] = 1
    if grid == new_grid:
        return 0
    
    white_cells = []
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == 1:
                white_cells.append((i, j))
    return white_cells

def color_cell(x, y, color):
    cell = (top_left_x + x*cell_size, top_left_y + y*cell_size, cell_size, cell_size)
    pygame.draw.rect(win, color, cell)

def create_grid(white_cells):
    grid = [[0 for w in range(50)] for x in range(50)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = 0
            if (i, j) in white_cells:
                grid[i][j] = 1
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)
            color_cell(i, j, color)
    
    return grid

def draw_grid(surface, rows, cols):
    for i in range(rows):
        pygame.draw.line(surface, (128, 128, 128), (top_left_x, top_left_y + i*cell_size), \
            (top_left_x + area_width, top_left_y + i*cell_size))
        for j in range(cols):
            pygame.draw.line(surface, (128, 128, 128), (top_left_x + j*cell_size, top_left_y), \
            (top_left_x + j*cell_size, top_left_y + area_height))


def main():

    # first white cells
    white_cells = [(1, 0),(2, 1),(0, 2),(1, 2),(2, 2)]

    while(white_cells != 0):
        grid = create_grid(white_cells)
        # draw gridlines
        draw_grid(win, 51, 51)
        pygame.display.update()
        white_cells = new_white_cells(grid)
        time.sleep(0.01)


def main_menu():
    
    win.fill((0,0,0))
    
    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        main()
	# event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
        



# initialize the pygame module
pygame.init()

# create a surface on screen that has the size of 500 x 500
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Conway's Game of Life")

main_menu()
