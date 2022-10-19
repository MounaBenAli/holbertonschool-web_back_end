#!/usr/bin/env python3
"""Unittests for utils.py a library for accessing github API."""

import unittest
from unittest.mock import patch, Mock

from defer import return_value
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """ Unittests for utils.access_nested_map() """
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


class TestGetJson(unittest.TestCase):
    """ Unittests for utils.get_json() """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests that get_json() returns JSON from mock test_url."""
        mock_request = Mock()
        mock_request.json.return_value = test_payload
        with patch('requests.get', return_value=mock_request):
            self.assertEqual(get_json(test_url), test_payload)
            mock_request.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Unittests for utils.memoize() """

    def test_memoize(self):
        """Tests memoization"""
        class TestClass:
            """Test"""

            def a_method(self):
                """Test a_method"""
                return 42

            @memoize
            def a_property(self):
                """Test memoization"""
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
