print("VIJITHA - 192124187")
print("travelling salesman")
import itertools
def distance(city1, city2):
    return distance_matrix[city1][city2]
def tsp_bruteforce(n, distance_matrix):
    min_distance = float('inf')
    best_path = None
    all_cities = list(range(n))
    permutations = itertools.permutations(all_cities)
    for path in permutations:
        total_distance = 0
        for i in range(n - 1):
            total_distance += distance(path[i], path[i + 1])
        total_distance += distance(path[-1], path[0])
        if total_distance < min_distance:
            min_distance = total_distance
            best_path = path
    return best_path, min_distance
distance_matrix = [
    [0, 19, 20, 21],
    [22, 0, 19, 18],
    [20, 15, 0, 25],
    [21, 14, 25, 0]
]
num_cities = len(distance_matrix)
best_path, min_distance = tsp_bruteforce(num_cities, distance_matrix)
print("distancematrix:",distance_matrix)
print("Best path:", best_path)
print("Minimum distance:", min_distance)
