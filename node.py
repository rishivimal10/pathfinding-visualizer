import pygame as pg

from colours import Colours
from manhattan_distance import manhattan_distance


class Node:

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x_coord = col * width
        self.y_coord = row * width
        self.width = width
        self.total_rows = total_rows
        self.colour = Colours.WHITE
        self.neighbours = []
        self.h_score = float('inf')

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == Colours.RED

    def is_open(self):
        return self.colour == Colours.TURQUOISE

    def is_barrier(self):
        return self.colour == Colours.BLACK

    def is_start(self):
        return self.colour == Colours.ORANGE

    def is_end(self):
        return self.colour == Colours.PURPLE

    def reset(self):
        self.colour = Colours.WHITE

    def make_start(self):
        self.colour = Colours.ORANGE

    def make_closed(self):
        self.colour = Colours.RED

    def make_open(self):
        self.colour = Colours.TURQUOISE

    def make_barrier(self):
        self.colour = Colours.BLACK

    def make_end(self):
        self.colour = Colours.PURPLE

    def make_path(self):
        self.colour = Colours.GREEN

    def draw(self, win):
        pg.draw.rect(win, self.colour.value, (self.x_coord, self.y_coord, self.width, self.width))

    def update_neighbours(self, grid):

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # CHECK DOWN
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # CHECK UP
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # CHECK RIGHT
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # CHECK LEFT
            self.neighbours.append(grid[self.row][self.col - 1])

    def set_h_score(self, end):
        self.h_score = manhattan_distance(self.get_pos(), end.get_pos())

    def get_h_score(self):
        return self.h_score
