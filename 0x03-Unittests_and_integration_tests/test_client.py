#!/usr/bin/env python3
""" Parameterize and patch as decorators """
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Test that GithubOrgClient org method returns the correct value."""
        github_client = GithubOrgClient(org_name)
        result = github_client.org()
        Expected_url = f"https://api.github.com/orgs/{org_name}"
        mock.assert_called_once_with(Expected_url)

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """ Test _public_repos_url method of GithubOrgClient class."""
        k_payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}
        mock_org.return_value = k_payload
        github_client = GithubOrgClient("testorg")

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = k_payload["repos_url"]
            result = github_client._public_repos_url
            self.assertEqual(result, k_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Method to unit-test GithubOrgClient.public_repos."""

        # Define a known payload to be returned by get_json
        known_payload = [{"name": "repo1"}, {"name": "repo2"}]

        # Mock get_json to return the known payload
        mock_get_json.return_value = known_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked:
            mocked.return_value = "school"
            # Create an instance of GithubOrgClient
            githuh_client = GithubOrgClient("testorg")

            # Call the public_repos method
            result = githuh_client.public_repos()

            expected_repos = ["repo1", "repo2"]
            self.assertEqual(result, expected_repos)

            mocked.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Method to unit-test GithubOrgClient.has_license. """
        github_client = GithubOrgClient("testorg")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)
