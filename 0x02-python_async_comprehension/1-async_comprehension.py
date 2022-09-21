#!/usr/bin/env python3
""" Async Generator """

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine called async_comprehension that takes no arguments.
    Collects 10 random numbers using an async comprehensing
    over async_generator.
    Returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
