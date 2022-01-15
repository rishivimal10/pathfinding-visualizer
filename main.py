import pygame as pg
import pygame.display

from astar_algorithm import astar_algorithm
from grid import make_grid, draw

GRID_WIDTH = 800
WIN = pg.display.set_mode((GRID_WIDTH, GRID_WIDTH))
pg.display.set_caption("Pathfinding Algorithm Visualization")


def get_clicked_pos(pos, rows, grid_width):
    cube_width = grid_width // rows
    x, y = pos

    row = y // cube_width
    col = x // cube_width

    return row, col


def main(win, grid_width):
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
                if event.key == pg.K_SPACE and not started:
                    started = True

                    for row in grid:
                        for node in row:
                            node.set_h_score(end)
                            node.update_neighbours(grid)

                    astar_algorithm(lambda: draw(win, grid, rows, grid_width), grid, start, end)

                if event.key == pg.K_c:
                    start = None
                    end = None
                    grid = make_grid(rows, grid_width)
                    started = False

    pygame.quit()


main(WIN, GRID_WIDTH)
