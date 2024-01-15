#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular
function syntax to do this) task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""
import asyncio
from typing import Generator
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for wait_random with the specified max_delay.

    Args:
    - max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
    - asyncio.Task: A task representing the execution of wait_random.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
