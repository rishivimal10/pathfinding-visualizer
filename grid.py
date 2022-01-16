import pygame as pg

from colours import Colours
from node import Node


def make_grid(rows, grid_width):
    grid = []
    cube_width = grid_width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            new_node = Node(i, j, cube_width, rows)
            grid[i].append(new_node)

    return grid


def draw_grid_lines(win, rows, grid_width):
    cube_width = grid_width // rows

    for i in range(rows):
        pg.draw.line(win, Colours.GREY.value, (0, i * cube_width), (grid_width, i * cube_width))

    for i in range(rows):
        pg.draw.line(win, Colours.GREY.value, (i * cube_width, 0), (i * cube_width, grid_width))


def draw(win, grid, rows, grid_width):
    win.fill(Colours.WHITE.value)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid_lines(win, rows, grid_width)
    pg.display.update()


def draw_found_path(came_from, end, draw_lambda_func):
    current = end
    while current in came_from:
        current = came_from[current]
        if current != end:
            current.make_path()
        draw_lambda_func()

    current.make_start()
