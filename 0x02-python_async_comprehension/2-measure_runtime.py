#!/usr/bin/env python3
""" Run time for four parallel comprehensions """

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine called measure_runtime that takes no arguments.
    Executes async_comprehension() four times in parallel using asyncio.gather.
    Measures the total runtime and return it.
    """
    run: List = []
    start: int = time.time()
    for i in range(4):
        run.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*run)
    run_time: int = time.time() - start
    return (run_time)
