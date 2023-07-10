#!/usr/bin/env python3
"""
task 2
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of all the delays"""
    delays_list = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(delays_list)