#!/usr/bin/env python3
""" Tasks """

import asyncio
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """a function task_wait_random that takes
       an integer max_delay.
       Returns a asyncio.Task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return (task)
