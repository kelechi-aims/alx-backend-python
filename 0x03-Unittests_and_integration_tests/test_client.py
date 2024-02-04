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
        """ Test that GithubOrgClient.org returns the correct value. """

        # Create an instance of GithubOrgClient with the provided org name
        github_client = GithubOrgClient(org_name)

        # Call the org method
        result = github_client.org()

        # Assert that get_json was called once with the expected argument
        Expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(Expected_url)
