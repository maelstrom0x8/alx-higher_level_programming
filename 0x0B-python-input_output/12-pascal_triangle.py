#!/usr/bin/python3

"""Pascal's Triangle Generator

This module provides a function for generating Pascal's
triangle up to the nth row.

Pascal's triangle is a mathematical construct where each number
in the triangle is the sum of the two numbers directly above it in
the previous row. The first and last numbers in each row are always 1,
and the rows are symmetric.

Functions:
    pascal_triangle(n): Generate Pascal's triangle up to the nth row.

Example:
    To generate Pascal's triangle up to the 5th row:
    >>> import pascal
    >>> result = pascal.pascal_triangle(5)
    >>> for row in result:
    ...     print(row)
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]

Args:
    n (int): The number of rows to generate in Pascal's triangle.

Returns:
    list: A list of lists representing Pascal's triangle. Each inner list
    corresponds to a row in the triangle.

Note:
    - If n is less than or equal to 0, an empty list is returned.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle. Each inner
        list corresponds to a row in the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
