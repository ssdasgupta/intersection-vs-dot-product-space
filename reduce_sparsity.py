import numpy as np

def reduce_sparsity(matrix, target_sparsity=0.95):
    """
    Reduce the sparsity of a matrix by randomly adding positive entries.
    Args:
        matrix: Input matrix to modify
        target_sparsity: Target sparsity ratio (between 0 and 1)
    Returns:
        Modified matrix with reduced sparsity
    """
    current_sparsity = np.count_nonzero(matrix == 0) / matrix.size
    if current_sparsity <= target_sparsity:
        return matrix
    
    # Calculate how many zeros to flip
    total_zeros = np.count_nonzero(matrix == 0)
    zeros_to_flip = int(total_zeros * (current_sparsity - target_sparsity))
    
    # Get indices of all zeros
    zero_indices = np.argwhere(matrix == 0)
    
    # Randomly select zeros to flip
    indices_to_flip = zero_indices[np.random.choice(len(zero_indices), zeros_to_flip, replace=False)]
    
    # Create a copy of the matrix and flip the selected zeros
    modified_matrix = matrix.copy()
    for idx in indices_to_flip:
        modified_matrix[tuple(idx)] = 1
    
    return modified_matrix

if __name__ == "__main__":
    # Example usage
    import numpy as np
    # Create a sample sparse matrix
    matrix = np.zeros((100, 100))
    matrix[0:10, 0:10] = 1  # Only 1% non-zero entries
    
    # Reduce sparsity to 95%
    modified_matrix = reduce_sparsity(matrix, target_sparsity=0.95)
    
    # Calculate and print sparsity
    original_sparsity = np.count_nonzero(matrix == 0) / matrix.size
    new_sparsity = np.count_nonzero(modified_matrix == 0) / modified_matrix.size
    
    print(f"Original sparsity: {original_sparsity:.2%}")
    print(f"New sparsity: {new_sparsity:.2%}") 