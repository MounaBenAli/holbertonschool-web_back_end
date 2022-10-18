#!/usr/bin/env python3
"""Unittests for utils.py a library for accessing github API."""

import unittest
from unittest import TestCase
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(TestCase):
    """ unit test for utils.access_nested_map """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected) -> Any:
        """Tests that the method returns what it is supposed to."""
        return self.assertEqual(access_nested_map(nested_map, path), expected)
