#!/usr/bin/env python3
"""
Learning Redis
"""
from matplotlib.backend_bases import key_press_handler
from pytest import param
import redis
import uuid
from typing import Union, Optional, Callable


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
        """Fetch data from redis"""
        data = self._redis.get(key)
        if not callable(fn):
            return data
        else:
            return fn(data)

    def get_str(self, key: str) -> str:
        """returns the key as an str value"""
        return str(self._redis.get(key), "UTF-8")

    def get_int(self, key: int) -> int:
        """returns the key as an int value"""
        return int(self._redis.get(key))
