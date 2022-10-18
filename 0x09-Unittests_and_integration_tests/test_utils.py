#!/usr/bin/env python3
"""Unittests for utils.py a library for accessing github API."""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """ unit test for utils.access_nested_map """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected) -> Any:
        """Tests that access_nested_map() returns what it is supposed to."""
        return self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",)),
            ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests if access_nested_map() raises an exception of type KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
