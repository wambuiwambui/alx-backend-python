#!/usr/bin/env python3
"""task 4"""
import asyncio


async def task_wait_random(max_delay: int) -> float:
    """Asynchronous function that waits for a random delay."""
    return await asyncio.create_task(wait_random(max_delay))
