#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    - multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that takes a float
    and returns the product.
    """
    def multiplier_function(x: float) -> float:
        """Callable multiplier function"""
        return x * multiplier

    return multiplier_function
