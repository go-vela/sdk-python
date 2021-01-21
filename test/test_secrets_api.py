# coding: utf-8
#
# Copyright (c) 2021 Target Brands, Inc. All rights reserved.

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vela
from vela.vela.secrets_api import SecretsApi  # noqa: E501
from vela.rest import ApiException


class TestSecretsApi(unittest.TestCase):
    """SecretsApi unit test stubs"""

    def setUp(self):
        self.api = SecretsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_secret(self):
        """Test case for create_secret

        """
        pass

    def test_delete_secret(self):
        """Test case for delete_secret

        Delete a secret from the configured backend.  # noqa: E501
        """
        pass

    def test_get_secret(self):
        """Test case for get_secret

        Retrieve a secret from the configured backend.  # noqa: E501
        """
        pass

    def test_get_secrets(self):
        """Test case for get_secrets

        Retrieve a list of secrets from the configured backend.  # noqa: E501
        """
        pass

    def test_update_secrets(self):
        """Test case for update_secrets

        Update a secret from the configured backend.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
