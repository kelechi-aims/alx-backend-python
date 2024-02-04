#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''Test that GithubOrgClient org method returns the correct value.'''
        github_client = GithubOrgClient(org_name)
        result = github_client.org()
        Expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(Expected_url)

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """ Test _public_repos_url method of GithubOrgClient class."""
        known_payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}
        mock_org.return_value = known_payload
        github_client = GithubOrgClient("testorg")

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            result = github_client._public_repos_url
            self.assertEqual(result, known_payload["repos_url"])
