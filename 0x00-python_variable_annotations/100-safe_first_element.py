#!/usr/bin/env python3
"""
Augment the following code with the correct duck-typed annotations
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of a sequence.

    Parameters:
    - lst (Sequence[Any]): The input sequence.

    Returns:
    Union[Any, None]: The first element of the sequence or None
    if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
