#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine called async_generator that takes no arguments.
    Loops 10 times, each time asynchronously wait 1 second,
    then yields a random number between 0 and 10.
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
