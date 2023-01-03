#!/usr/bin/python3
"""
Pascale triangle
"""


def fact(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod


def pascal_triangle(n):
    """
    pascal triangle using python
    """
    if n <= 0:
        return []
    List_1 = []
    for i in range(n):
        List_2 = []
        for j in range(i + 1):
            List_2.append(fact(i)//(fact(j) * fact(i - j)))
        List_1.append(List_2)
    return List_1
