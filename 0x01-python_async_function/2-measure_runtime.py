#!/usr/bin/env python3
""" Measures the runtime """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """a function measure_time that takes
       in 2 int arguments (in this order): n and max_delay.
       Measures the total execution time for wait_n(n, max_delay).
       Returns total_time / n (float)
    """

    start: int = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time: int = time.time() - start
    return (total_time / n)
