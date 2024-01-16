#!/usr/bin/env python3
""" Write a coroutine called async_generator that takes no arguments. """
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator coroutine that yields random
    float values between 0 and 10.

    Yields:
    - float: A random float between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
