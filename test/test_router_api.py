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
from vela.vela.router_api import RouterApi  # noqa: E501
from vela.rest import ApiException


class TestRouterApi(unittest.TestCase):
    """RouterApi unit test stubs"""

    def setUp(self):
        self.api = RouterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_base_metrics(self):
        """Test case for base_metrics

        """
        pass

    def test_get_badge(self):
        """Test case for get_badge

        """
        pass

    def test_health(self):
        """Test case for health

        """
        pass

    def test_post_webhook(self):
        """Test case for post_webhook

        """
        pass

    def test_version(self):
        """Test case for version

        """
        pass


if __name__ == '__main__':
    unittest.main()
