import pytest
import numpy as np
from my_lin_alg import my_transpose, my_mat_prod


def test_transpose():
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9],
         [1, 4, 2],
         [3, 11, 5]]
    custom_transpose = my_transpose(X)
    numpy_transpose = np.transpose(X).tolist()
    name1 = "Transpose implementation doesn't match NumPy"
    assert custom_transpose == numpy_transpose, name1


def test_matrix_multiplication():
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9],
         [1, 4, 2],
         [3, 11, 5]]
    Y = [[5, 8, 1, 2],
         [6, 7, 3, 0],
         [4, 5, 9, 1]]
    custom_product = my_mat_prod(X, Y)
    numpy_product = np.dot(X, Y).tolist()
    name2 = "Matrix multiplication implementation doesn't match NumPy"
    assert custom_product == numpy_product, name2


def test_matrix_multiplication_incompatible_sizes():
    X = [[1, 2, 3], [4, 5, 6]]
    Y = [[1, 2], [3, 4], [5, 6], [7, 8]]
    with pytest.raises(ValueError) as exc_info:
        my_mat_prod(X, Y)
    name3 = "Incompatible matrix dimensions:(2x3) and (4x2)"
    assert str(exc_info.value) == name3


def test_transpose_properties():
    # Test: transpose of transpose is the original matrix
    X = [[1, 2, 3], [4, 5, 6]]
    assert my_transpose(my_transpose(X)) == X


def test_matrix_multiplication_properties():
    # Test: multiplication with identity matrix
    X = [[1, 2], [3, 4]]
    Ident = [[1, 0], [0, 1]]
    assert my_mat_prod(X, Ident) == X
    assert my_mat_prod(Ident, X) == X


def test_randomized_multiplication():
    # Randomized test
    for _ in range(10):  # Run 10 random tests
        m, n, p = np.random.randint(1, 10, size=3)
        X = np.random.randint(0, 100, size=(m, n)).tolist()
        Y = np.random.randint(0, 100, size=(n, p)).tolist()
        custom_result = my_mat_prod(X, Y)
        numpy_result = np.dot(X, Y).tolist()
        name4 = "Random matrix multiplication test failed"
        assert custom_result == numpy_result, name4


def test_edge_cases():
    # Test: empty matrix
    assert my_transpose([[]]) == []
    # Test: 1x1 matrix
    assert my_transpose([[5]]) == [[5]]
    # Test: multiplication with zero matrix
    X = [[1, 2], [3, 4]]
    Z = [[0, 0], [0, 0]]
    assert my_mat_prod(X, Z) == [[0, 0], [0, 0]]
