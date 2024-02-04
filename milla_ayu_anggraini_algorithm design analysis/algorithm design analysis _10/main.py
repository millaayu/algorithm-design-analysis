from queue import PriorityQueue

def tsp(graph, start):
    num_cities = len(graph)
    visited = set()
    pq = PriorityQueue()
    pq.put((0, [start]))

    while not pq.empty():
        (cost, path) = pq.get()
        current_city = path[-1]

        if len(path) == num_cities:
            return (cost, path + [start])

        visited.add(current_city)

        for neighbor, neighbor_cost in enumerate(graph[current_city]):
            if neighbor not in visited and neighbor_cost > 0:
                new_cost = cost + neighbor_cost
                new_path = path + [neighbor]
                pq.put((new_cost, new_path))

    return "No solution"

graph = [
    [0, 7, 5, 0],  # Kota A
    [4, 0, 0, 8],  # Kota B
    [3, 5, 0, 5],  # Kota C
    [9, 0, 4, 0]   # Kota D
]

start_city = 0  # Kota A
min_cost, min_path = tsp(graph, start_city)

print("Jalur terpendek:", min_path)
print("Jarak terpendek:", min_cost)
