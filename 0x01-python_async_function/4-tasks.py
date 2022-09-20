#!/usr/bin/env python3
""" Tasks """

import asyncio
from asyncio import Task
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Alter code from wait_n() into a new function task_wait_n()
    """

    delays: List = []
    wait: List = []

    for i in range(n):
        delays.append(asyncio.ensure_future(task_wait_random(max_delay)))
    await asyncio.gather(*delays)
    for i in asyncio.as_completed(delays):
        wait.append(await i)
    return (wait)
