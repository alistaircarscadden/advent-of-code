from dataclasses import dataclass


@dataclass
class Node:
    elevation: int
    edges: list["Node"]
    min_distance: int


with open("input") as f:
    lines = f.readlines()

# create grid of nodes with elevation and empty edges list
grid = []
start_node = None
end_node = None
for line in lines:
    row = []
    for x in line:
        if x == "S":
            node = Node(
                elevation=ord("a"),
                edges=[],
                min_distance=0,
            )
            start_node = node
        elif x == "E":
            node = Node(
                elevation=ord("z"),
                edges=[],
                min_distance=1000000000,
            )
            end_node = node
        else:
            node = Node(
                elevation=ord(x),
                edges=[],
                min_distance=1000000000,
            )
        row.append(node)
    grid.append(row)

grid_height = len(grid)
grid_width = len(grid[0])

# fill each nodes edges list
for y in range(grid_height):
    for x in range(grid_width):
        here = grid[y][x]

        if x - 1 >= 0:
            neigh = grid[y][x - 1]
            if here.elevation >= neigh.elevation - 1:
                here.edges.append(neigh)
        if y - 1 >= 0:
            neigh = grid[y - 1][x]
            if here.elevation >= neigh.elevation - 1:
                here.edges.append(neigh)
        if x + 1 < grid_width:
            neigh = grid[y][x + 1]
            if here.elevation >= neigh.elevation - 1:
                here.edges.append(neigh)
        if y + 1 < grid_height:
            neigh = grid[y + 1][x]
            if here.elevation >= neigh.elevation - 1:
                here.edges.append(neigh)

# solve shortest path
queue = []

# part2: now make all "a" have min_distance 0 and push them all to the queue
for y in range(grid_height):
    for x in range(grid_width):
        here = grid[y][x]
        if here.elevation == ord("a"):
            here.min_distance = 0
            queue.append(here)

while len(queue) > 0:
    node = queue.pop()
    for neigh in node.edges:
        steps_to_nei = node.min_distance + 1
        if neigh.min_distance > steps_to_nei:
            neigh.min_distance = steps_to_nei
            queue.append(neigh)

print(end_node.min_distance)