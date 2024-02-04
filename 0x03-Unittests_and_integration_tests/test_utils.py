#!/usr/bin/env python3
""" Parameterize a unit test """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Test class that inherits from unittest.TestCase """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test the access_nested_map method returns what is expected """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a", 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Use the assertRaises context manager to test that a KeyError
        is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Implements the test_get_json method to test that
    utils.get_json returns the expected result.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Method to test that utils.get_json returns the expected result.
        """
        mocked_get = Mock()
        mocked_get.json.return_value = test_payload
        with patch('utils.requests.get', return_value=mocked_get) as mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator
    """
    def test_memoize(self):
        """ Test the memoize decorator """
        class TestClass:
            """
            Test class with a_method and a_property decorated with memoize.
            """
            def a_method(self):
                """ A method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ A property that calls a_method """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            mock_a_method.assert_called_once()
