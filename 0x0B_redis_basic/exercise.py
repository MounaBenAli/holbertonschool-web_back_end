#!/usr/bin/env python3
"""
Learning Redis
"""
from matplotlib.backend_bases import key_press_handler
from pytest import param
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Increments the count for that key every time the method is called
        & Returns the value returned by the original method.
    """
    __qualname__ = key


class Cache():
    """class Cache redis"""

    def __init__(self):
        """instance initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in redis cache in a key-value pair"""
        k = str(uuid.uuid4())
        self._redis.mset({k: data})

        return k

    def get(self, key: str, fn: Optional[Callable]
            ) -> Union[str, bytes, int, float]:
        """Fetch data from redis cache"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, str: str) -> str:
        """returns the key as an str value"""
        return str.decode(encoding='UTF-8',errors='strict')

    def get_int(self, key: int) -> int:
        """returns the key as an int value"""
        return int(self._redis.get(key))
