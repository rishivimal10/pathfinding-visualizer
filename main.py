import sys

import pygame as pg
import pygame.display

from astar_algorithm import astar_algorithm
from colours import Colours
from dijkstras_algorithm import dijkstras_algorithm
from grid import make_grid, draw
from supported_algorithms import Algorithms
from greedy_bfs_algorithm import greedy_bfs

GRID_WIDTH = 750
WIN = pg.display.set_mode((GRID_WIDTH, GRID_WIDTH))
pg.display.set_caption("Pathfinding Algorithm Visualization")


def get_clicked_pos(pos, rows, grid_width):
    cube_width = grid_width // rows
    x, y = pos

    row = y // cube_width
    col = x // cube_width

    return row, col


def button(win, position, text):
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 25)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(win, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(win, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(win, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(win, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(win, (100, 100, 100), (x, y, w , h))
    return win.blit(text_render, (x, y))


def main_menu(win):
    run = True
    while run:
        win.fill(Colours.BLACK.value)
        b1 = button(win, (300, 300), "Dijkstra's Algorithm")
        b2 = button(win, (300, 350), "A* Search")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pg.display.set_caption("Dijkstra's Algorithm")
                    main(win, GRID_WIDTH, Algorithms.DIJKSTRAS)
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    pg.display.set_caption("A* Search")
                    main(win, GRID_WIDTH, Algorithms.A_STAR)
        pg.display.update()
    pg.quit()


def main(win, grid_width, algorithm: Algorithms):
    rows = 50
    grid = make_grid(rows, grid_width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, rows, grid_width)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, grid_width)
                    started = False

                if event.key == pg.K_ESCAPE:
                    run = False

            if started:
                continue

            if pg.mouse.get_pressed()[0]:
                pos = pg.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, grid_width)
                node = grid[row][col]
                if not start:
                    start = node
                    node.make_start()

                elif not end:
                    if not node.is_start():
                        end = node
                        node.make_end()

                else:
                    if not node.is_start() and not node.is_end():
                        node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pg.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, grid_width)
                node = grid[row][col]

                if node.is_start():
                    start = None
                    node.reset()

                elif node.is_end():
                    end = None
                    node.reset()

                elif node.is_barrier():
                    node.reset()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not started and start and end:
                    started = True

                    for row in grid:
                        for node in row:
                            node.set_h_score(end)
                            node.update_neighbours(grid)

                    if algorithm == Algorithms.A_STAR:
                        greedy_bfs(lambda: draw(win, grid, rows, grid_width), grid, start, end)

                    elif algorithm == Algorithms.DIJKSTRAS:
                        dijkstras_algorithm(lambda: draw(win, grid, rows, grid_width), grid, start, end)


main_menu(WIN)
