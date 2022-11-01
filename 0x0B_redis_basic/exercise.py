#!/usr/bin/env python3
"""
Learning Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps
import sys


def count_calls(method: Callable) -> Callable:
    """Counts the number of calls for the methods inside the cache class
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper for method"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores history of inputs/outputs for a method in a list
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper for method"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> Callable:
    """Displays the history of calls of a particular function.
    """
    pass


class Cache():
    """class Cache redis"""

    def __init__(self):
        """instance initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis cache in a key-value pair"""
        k = str(uuid.uuid4())
        self._redis.mset({k: data})

        return k

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """Fetch data from redis cache"""

        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, str: str) -> str:
        """returns the key as an str"""
        return str.decode(encoding='UTF-8', errors='strict')

    def get_int(self, key: bytes) -> int:
        """returns the key as an int"""
        return int.from_bytes(key, sys.byteorder, signed=False)
