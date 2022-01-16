from queue import PriorityQueue
import pygame as pg

from grid import draw_found_path


def greedy_bfs(draw, grid, start, end):
    count = 0
    open_set_queue = PriorityQueue()
    open_set_queue.put((start.get_h_score(), count, start))
    heuristic_distance_to_end = {node: float('inf') for row in grid for node in row}
    heuristic_distance_to_end[start] = start.get_h_score()
    came_from ={}

    open_set_set = {start}

    while not open_set_queue.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        current = open_set_queue.get()[2]
        open_set_set.remove(current)

        if current == end:
            draw_found_path(came_from, end, draw)
            current.make_end()
            return True

        for neighbour in current.neighbours:
            heuristic_distance_to_end[neighbour] = neighbour.get_h_score()
            came_from[neighbour] = current

            if neighbour not in open_set_set:
                count += 1
                open_set_queue.put((heuristic_distance_to_end[neighbour], count, neighbour))
                open_set_set.add(neighbour)
                neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False
