#!/usr/bin/env python3
""" Auth Module for the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """handle path authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request"""
        return None
