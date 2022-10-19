#!/usr/bin/env python3
"""Unittests for client.py a client for the github API."""

import unittest
from unittest.mock import patch, PropertyMock
from defer import return_value
from parameterized import parameterized
from client import GithubOrgClient
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

    def test_public_repos_url(self):
        """unit-test GithubOrgClient._public_repos_url"""
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
        ) as mock_property:
            mock_property.return_value = {"repos_url": "https://example.com"}
            self.assertEqual(
                GithubOrgClient('test')._public_repos_url,
                "https://example.com")

    def test_public_repos(self):
        """unit-test GithubOrgClient.public_repos"""
        with patch(
            'client.get_json', new_callable=PropertyMock
        ) as mock_json:
            mock_json.return_value = {"repos_url": "https://example.com"}
            self.assertEqual(
                GithubOrgClient('test')._public_repos_url,
                "https://example.com")
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, result):
        """unit-test GithubOrgClient.has_license"""
        test = GithubOrgClient('test')
        self.assertEqual(test.has_license(repo, license_key), result)


if __name__ == '__main__':
    unittest.main()
