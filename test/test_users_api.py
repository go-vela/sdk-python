# coding: utf-8

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.4.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vela
from vela.vela.users_api import UsersApi  # noqa: E501
from vela.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_token(self):
        """Test case for create_token

        """
        pass

    def test_create_user(self):
        """Test case for create_user

        """
        pass

    def test_delete_token(self):
        """Test case for delete_token

        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        """
        pass

    def test_get_user(self):
        """Test case for get_user

        """
        pass

    def test_get_user_source_repos(self):
        """Test case for get_user_source_repos

        """
        pass

    def test_get_users(self):
        """Test case for get_users

        """
        pass

    def test_update_current_user(self):
        """Test case for update_current_user

        """
        pass

    def test_update_user(self):
        """Test case for update_user

        """
        pass


if __name__ == '__main__':
    unittest.main()
