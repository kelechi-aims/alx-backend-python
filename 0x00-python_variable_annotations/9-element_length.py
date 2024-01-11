#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values with the
appropriate types
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element from the input list
    and its corresponding length.

    Parameters:
    - lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
    an element from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
