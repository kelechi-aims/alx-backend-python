#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with
    the specified max_delay.

    Args:
    - n (int): Number of times to spawn wait_random.
    - max_delay (int): Maximum delay in seconds for each wait_random.

    Returns:
    - List[float]: List of delays in ascending order.
    """
    task = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*task)
    return sorted(results)
