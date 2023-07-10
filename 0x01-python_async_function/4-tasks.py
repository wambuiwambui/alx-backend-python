#!/usr/bin/env python3
"""
task 4
"""

import asyncio
from typing import List
from random import uniform


async def task_wait_random(max_delay: int) -> float:
    """Asynchronous function that waits for a random delay."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that returns a list of all the delays.

    Args:
        n (int): The number of tasks.
        max_delay (int): The maximum delay.

    Returns:
        List[float]: A list of all the delays.

    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
