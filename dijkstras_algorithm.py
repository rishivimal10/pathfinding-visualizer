from queue import PriorityQueue
import pygame as pg

from grid import draw_found_path


def dijkstras_algorithm(draw, grid, start, end):
    count = 0
    open_set_queue = PriorityQueue()
    open_set_queue.put((0, count, start))
    distance_from_start = {node: float('inf') for row in grid for node in row}
    distance_from_start[start] = 0
    came_from = {}

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
            temp_score = distance_from_start[current] + 1

            if temp_score < distance_from_start[neighbour]:
                distance_from_start[neighbour] = temp_score
                came_from[neighbour] = current
                if neighbour not in open_set_set:
                    count += 1
                    open_set_queue.put((distance_from_start[neighbour], count, neighbour))
                    open_set_set.add(neighbour)

                    if not neighbour.is_end():
                        neighbour.make_open()
        draw()

        if current != start:
            current.make_closed()

    return False
