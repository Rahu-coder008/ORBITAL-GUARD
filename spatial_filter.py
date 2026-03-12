import numpy as np
from collections import defaultdict

def find_candidate_pairs(positions, threshold=100.0):
    """
    Filters 50,000+ objects using 3D Spatial Hashing.
    Returns a list of index pairs (i, j) that are within the threshold.
    """
    cell_size = threshold
    grid = defaultdict(list)
    
    # Hash objects into grid cells
    cell_coords = np.floor(positions / cell_size).astype(int)
    for i, cell in enumerate(cell_coords):
        grid[tuple(cell)].append(i)
        
    candidate_pairs = set()
    offsets = np.array(np.meshgrid([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])).T.reshape(-1, 3)
    
    # Check current cell and neighbors
    for cell, indices in grid.items():
        cell_vec = np.array(cell)
        for offset in offsets:
            neighbor_cell = tuple(cell_vec + offset)
            if neighbor_cell in grid:
                neighbor_indices = grid[neighbor_cell]
                for i in indices:
                    for j in neighbor_indices:
                        if i < j:  
                            candidate_pairs.add((i, j))
                            
    return list(candidate_pairs)