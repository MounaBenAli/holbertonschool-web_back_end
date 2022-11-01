#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""
import redis
import requests
from functools import wraps


def get_page(url: str) -> str:
    """Returns HTML content from URL
    """
    pass
