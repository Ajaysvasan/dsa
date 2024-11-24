import sys

def to_be_visited(visited_and_distance):
    """
    Find the next vertex to visit.
    """
    min_distance = sys.maxsize
    v = -1
    for index in range(number_of_vertices):
        if not visited_and_distance[index][0] and visited_and_distance[index][1] <= min_distance:
            min_distance = visited_and_distance[index][1]
            v = index
    return v

# Graph representation (adjacency matrix for edges and connections)
vertices = [[0, 1, 1, 0], 
            [0, 0, 1, 0], 
            [0, 0, 0, 1], 
            [0, 0, 0, 0]]

edges = [[0, 3, 4, 0], 
         [0, 0, 0.5, 0], 
         [0, 0, 0, 1], 
         [0, 0, 0, 0]]

number_of_vertices = len(vertices)

# Initialize visited and distance table
visited_and_distance = [[0, 0]]  # [visited (0/1), distance]
for i in range(1, number_of_vertices):
    visited_and_distance.append([0, sys.maxsize])

# Dijkstra's algorithm
for _ in range(number_of_vertices):
    # Find the next vertex to visit
    to_visit = to_be_visited(visited_and_distance)
    if to_visit == -1:  # No more vertices to visit
        break

    for neighbor_index in range(number_of_vertices):
        if vertices[to_visit][neighbor_index] == 1 and not visited_and_distance[neighbor_index][0]:
            # Calculate new distance
            new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
            if visited_and_distance[neighbor_index][1] > new_distance:
                visited_and_distance[neighbor_index][1] = new_distance

    # Mark the current vertex as visited
    visited_and_distance[to_visit][0] = 1

# Print shortest distances
for i, distance in enumerate(visited_and_distance):
    print(f"The shortest distance of {chr(ord('a') + i)} from the source vertex 'a' is: {distance[1]}")
