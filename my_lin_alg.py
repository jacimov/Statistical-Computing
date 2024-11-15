"""
This module contains functions of matrix transpose.
It also has matrix multiplication operations.
"""

# Matrix transpose function
# Input: X - a matrix represented as a list of lists
# Output: The transpose of X, where rows become columns and vice versa


def my_transpose(X):
    # Calculate the number of rows and columns
    num_rows = len(X)
    num_cols = len(X[0]) if X else 0

    # Initialize the transposed matrix
    transposed = [[] for _ in range(num_cols)]

    # Fill in the transposed matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j].append(X[i][j])

    return transposed


# Matrix multiplication function
# Inputs: X, Y - matrices represented as lists of lists
# Output: The product of X and Y, assuming they have compatible dimensions


def my_mat_prod(X, Y):
    # Get dimensions of input matrices
    X_rows = len(X)
    X_cols = len(X[0]) if X else 0
    Y_rows = len(Y)
    Y_cols = len(Y[0]) if Y else 0

    # Check if matrices have compatible dimensions
    if X_cols != Y_rows:
        name1 = f"Incompatible matrix dimensions:({X_rows}x{X_cols})"
        name2 = f" and ({Y_rows}x{Y_cols})"
        raise ValueError(name1 + name2)

    # Initialize the result matrix
    result = [[0 for _ in range(Y_cols)] for _ in range(X_rows)]

    # Perform matrix multiplication
    for i in range(X_rows):
        for j in range(Y_cols):
            for k in range(X_cols):
                # Multiply corresponding elements
                result[i][j] += X[i][k] * Y[k][j]

    return result
