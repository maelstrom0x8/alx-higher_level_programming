#!/usr/bin/python3

"""
This module defines a function 'matrix_divided' for dividing a matrix by a
specified divisor. It returns a new matrix with each element divided by
the divisor, rounded to two decimal places.

Functions:
    - matrix_divided(matrix, div): Divide a matrix by a
    divisor and return the result as a new matrix.

Note:
    - The 'matrix_divided' function performs element-wise division and
    rounds the result to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divide a matrix by a divisor and return the result as a new matrix.
    Each element in the input matrix is divided by the specified divisor,
    and the result is rounded to two decimal places.

    Args:
        matrix (list of lists): The matrix to be divided, represented as
        a list of lists containing integers or floats.
        div (int or float): The divisor used for the division operation.

    Returns:
        list of lists: A new matrix where each element is the result of the
        corresponding element in the input matrix divided by the divisor.

    Raises:
        TypeError: If 'matrix' is not a valid matrix (list of lists) of
        integers/floats, if 'div' is not a number, or if rows of the matrix
        have different sizes.
        ZeroDivisionError: If 'div' is zero.
        Note:
        - The 'matrix_divided' function performs element-wise division and
        rounds the result to two decimal places.
    """
    rows = []
    if (
        matrix == []
        or not isinstance(matrix, list)
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            (isinstance(e, int) or isinstance(e, float))
            for e in [num for row in matrix for num in row]
        )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    dimension = len(matrix[0])
    for e in range(len(matrix)):
        if len(matrix[e]) != dimension:
            raise TypeError("Each row of the matrix must have the same size")
        col = [round(x / div, 2) for x in matrix[e]]
        rows.append(col)

    return rows
