#!/usr/bin/env python3
"""Unittests for client.py a client for the github API."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class TestGithubOrgClient(unittest.TestCase):
    """ Unittests for the class GithubOrgClient"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock):
        """ Tests that GithubOrgClient.org returns the correct value"""
        url = 'https://api.github.com/orgs/{}'.format(org_name)
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org, {'key': 'value'})
        mock.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
