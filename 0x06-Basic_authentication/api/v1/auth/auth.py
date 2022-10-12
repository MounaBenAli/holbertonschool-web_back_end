#!/usr/bin/env python3
""" Auth Module for the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths """
        return False

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request"""
        return None
