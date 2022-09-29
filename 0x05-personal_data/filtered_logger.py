#!/usr/bin/env python3
""" Regex-ing """

import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns the log message obfuscated(difficult to understand)"""
    for field in fields:
        message = re.sub(
            F"{field}=.+?{separator}",
            F"{field}={redaction}{separator}",
            message)
    return message
