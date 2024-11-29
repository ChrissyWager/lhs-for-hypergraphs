import numpy as np
import os

def to_adjacency_dict(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # First line contains the metrics that we can ignore
    num_hyperedges, num_vertices = map(int, lines[0].strip().split())
    
    # Will turn the hgf data into an adjacency dictionary
    adjacency = {i: [] for i in range(1, num_vertices + 1)}
    hyperedges = {i: [] for i in range(1, num_hyperedges + 1)}
    
    # Parse the remaining lines
    for line in lines[1:]:
        if line.strip():
            source, _, target = line.partition('=')
            source = int(source.strip())
            target = int(target.strip())
            
            # Add to adjacency lists
            adjacency[target].append(source)  # Vertex points to hyperedge
            hyperedges[source].append(target)  # Hyperedge points to vertex
    
    return adjacency, hyperedges

# Alternative to adjacency dictionaries
def to_incidence_matrix(adjacency, num_hyperedges, num_vertices):
    # Initialize a binary incidence matrix
    matrix = np.zeros((num_vertices, num_hyperedges), dtype=int)
    
    for vertex, edges in adjacency.items():
        for edge in edges:
            matrix[vertex - 1, edge - 1] = 1  # Convert to 0-based index
    
    return matrix

# Get the current directory
script_dir = os.path.dirname(__file__)

# Construct the full path to the dataset to be used
file_path = os.path.join(script_dir, 'got.hgf')

# Parse the dataset
adjacency, hyperedges = to_adjacency_dict(file_path)
print("Adjacency:", adjacency)
print("Hyperedges:", hyperedges)

# Convert to an incidence matrix if desired
num_vertices = len(adjacency)
num_hyperedges = len(hyperedges)
matrix = to_incidence_matrix(adjacency, num_hyperedges, num_vertices)
print("Incidence Matrix:\n", matrix)