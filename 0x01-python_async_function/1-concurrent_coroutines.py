#!/usr/bin/env python3
""" executes multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """an asynchronous coroutine wait_n that takes
       in 2 int arguments (in this order): n and max_delay.
       Spawns wait_random n times with the specified max_delay.
       Returns the list of all the delays (float values) in ascending order.
    """
    delays: List = []
    wait: List = []

    for i in range(n):
        delays.append(asyncio.ensure_future(wait_random(max_delay)))
    await asyncio.gather(*delays)
    for i in asyncio.as_completed(delays):
        wait.append(await i)
    return (wait)
