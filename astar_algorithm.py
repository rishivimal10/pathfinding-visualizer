from queue import PriorityQueue

import pygame
import pygame as pg

from grid import draw_found_path


def astar_algorithm(draw, grid, start, end):
    count = 0
    open_set_queue = PriorityQueue()
    open_set_queue.put((0, count, start))
    g_score = {node: float('inf') for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float('inf') for row in grid for node in row}
    f_score[start] = start.get_h_score()
    came_from = {}

    open_set_set = {start}

    while not open_set_queue.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pygame.quit()

        current = open_set_queue.get()[2]
        open_set_set.remove(current)

        if current == end:
            draw_found_path(came_from, end, draw)
            current.make_end()
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = g_score[neighbour] + neighbour.get_h_score()
                came_from[neighbour] = current
                if neighbour not in open_set_set:
                    count += 1
                    open_set_queue.put((f_score[neighbour], count, neighbour))
                    open_set_set.add(neighbour)
                    neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
