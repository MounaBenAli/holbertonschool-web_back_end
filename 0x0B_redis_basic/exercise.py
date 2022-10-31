#!/usr/bin/env python3
"""
Learning Redis
"""
import redis
import uuid
from typing import Union


class Cache():
    """class Cache redis"""

    def __init__(self):
        """instance initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and store it in redis"""
        k = str(uuid.uuid4())
        self._redis.mset({k: data})

        return k
