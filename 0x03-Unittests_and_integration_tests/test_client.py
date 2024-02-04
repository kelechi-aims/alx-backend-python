#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ Test the org method """
        github_client = GithubOrgClient(org_name)
        result = github_client.org()
        Expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(Expected_url)
