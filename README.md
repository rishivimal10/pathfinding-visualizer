# Pathfinding Visualizer

This project uses Python and Pygame to visualize pathfinding algorithms. Currently supports Dijkstra's Algorithm and A* Search.

Example Result of A* Search:

<img width="500" alt="Screen Shot 2022-01-15 at 5 52 24 PM" src="https://user-images.githubusercontent.com/56571102/149640127-23496bbd-a847-4ad7-87c9-5ef35f9566ec.png">

(orange = start, blue = end, black = barrier, purple = shortest path, red = closed node, green = open node)


## How to use

1. Choose which algorithm you would like to visualize
2. Left-click on any square on the grid to choose the starting spot. This will be represented by the colour orange
3. Left-click again on a different square to choose the destination. This will be represented by the colour blue
4. Any subsequent left-clicks will create barriers on the square. These will be represented by the colour black
5. Right-click on any square to reset it.
6. Once the start, end, and barriers are set, press SPACE to start the algorithm
7. Once the algorithm is done, the shortest path, if it exists, will be shown in purple
8. Press 'c' at any time (while the algorithm is not running) to reset the whole grid
9. Press ESC at any time to go back to the main menu

## Supported Algorithms

### Dijkstra's Algorithm
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm

This implementation of Djikstra's algorithm uses a Priority Queue which is prioritized by the distance from the start node to the current node. Dijkstra's is an uninformed search algorithm, but it guarantees the shortest path.

### A* Search
https://en.wikipedia.org/wiki/A*_search_algorithm

A* search is very similar to Dijkstra's algorithm except it uses a heuristic to inform the searching. Instead of the Priority Queue being prioritized by only the distance from the start node to the current node, the queue is prioritized by f_score, which is calculated by adding the distance from the start node to the current node with the estimated distance to the end node (this implementation estimated distance by calculating manhattan distance)
