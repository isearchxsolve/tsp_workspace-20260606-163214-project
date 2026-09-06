import numpy as np
from scipy.spatial import distance

def tsp_solver(graph):
    # Initialize the path with the first node
    path = [0]
    visited = set([0])
    current_node = 0
    
    # Loop until all nodes are visited
    while len(visited) < len(graph):
        # Find the closest unvisited node
        min_distance = float('inf')
        next_node = None
        for i in range(len(graph)):
            if i not in visited and distance.euclidean(graph[current_node], graph[i]) < min_distance:
                min_distance = distance.euclidean(graph[current_node], graph[i])
                next_node = i
        
        # Add the closest node to the path and mark it as visited
        path.append(next_node)
        visited.add(next_node)
        current_node = next_node
    
    # Add the distance from the last node back to the first node to complete the cycle
    path.append(0)
    return path

def main():
    # Define the graph as a list of node coordinates
    graph = np.array([[0, 0], [10, 0], [5, 3], [0, 5]])
    path = tsp_solver(graph)
    print(path)

if __name__ == '__main__':
    main()