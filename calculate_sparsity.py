import numpy as np

def calculate_sparsity(matrix):
    """
    Calculate the sparsity of a matrix (percentage of zero elements).
    """
    total_elements = matrix.size
    zero_elements = np.count_nonzero(matrix == 0)
    sparsity = (zero_elements / total_elements) * 100
    return sparsity

# Load the matrices
Mui_dot = np.load('data/Mui_dot.npy')
Mui_set = np.load('data/Mui_set.npy')

# Calculate sparsity for both matrices
sparsity_dot = calculate_sparsity(Mui_dot)
sparsity_set = calculate_sparsity(Mui_set)

print(f"Sparsity of Mui_dot: {sparsity_dot:.2f}%")
print(f"Sparsity of Mui_set: {sparsity_set:.2f}%")
print(f"Number of non-zero elements in Mui_dot: {np.count_nonzero(Mui_dot)}")
print(f"Number of non-zero elements in Mui_set: {np.count_nonzero(Mui_set)}")
print(f"Total elements in matrix: {Mui_dot.size}") 