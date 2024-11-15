"""
This module tests the my matrix operations functions against NumPy.
"""

import numpy as np
# The command below allows you to call my_transpose and my_mat_prod as if they
# were functions defined within this module
from my_lin_alg import my_transpose, my_mat_prod

# Function to compare results


def compare_results(custom_result, numpy_result, operation_name):
    if np.allclose(custom_result, numpy_result):
        print(f"{operation_name}: Custom implementation matches NumPy")
    else:
        print(f"{operation_name}: Custom implementation does not match NumPy")
        print("Custom result:")
        print(custom_result)
        print("NumPy result:")
        print(numpy_result)

# 5x3 matrix


X = np.array(
    [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9],
     [1, 4, 2],
     [3, 11, 5]])

# 3x4 matrix


Y = np.array(
    [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]])

# Test transpose
custom_transpose = my_transpose(X.tolist())
numpy_transpose = np.transpose(X)
compare_results(custom_transpose, numpy_transpose, "Transpose")

# Test matrix multiplication
custom_product = my_mat_prod(X.tolist(), Y.tolist())
numpy_product = np.dot(X, Y)
compare_results(custom_product, numpy_product, "Matrix Multiplication")
