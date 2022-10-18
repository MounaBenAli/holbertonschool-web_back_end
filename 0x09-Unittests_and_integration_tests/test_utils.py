#!/usr/bin/env python3
"""Unittests for utils.py a library for accessing github API."""

from unittest import TestCase
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """ unit test for utils.access_nested_map """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",)),
            ({"a": {"b": 2}}, ("a",)),
            ({"a": {"b": 2}}, ("a", "b"))
        ]
    )
    def access_nested_map(self, nested_map, path, expected):
        """Tests that the method returns what it is supposed to."""
        return self.assertEqual(access_nested_map(nested_map, path), expected)
