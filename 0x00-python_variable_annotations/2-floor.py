#!/usr/bin/env python3
"""
Write a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""
import math


def floor(n: float) -> float:
    """
    Returns the floor of a floating-point number.

    Parameters:
    - n (float): The input floating-point number.

    Returns:
    int: The floor of the input number.
    """
    return math.floor(n)
