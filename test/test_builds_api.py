# coding: utf-8
#
# Copyright (c) 2022 Target Brands, Inc. All rights reserved.

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vela
from vela.vela.builds_api import BuildsApi  # noqa: E501
from vela.rest import ApiException


class TestBuildsApi(unittest.TestCase):
    """BuildsApi unit test stubs"""

    def setUp(self):
        self.api = BuildsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_build(self):
        """Test case for create_build

        """
        pass

    def test_delete_build(self):
        """Test case for delete_build

        """
        pass

    def test_get_build(self):
        """Test case for get_build

        """
        pass

    def test_get_build_logs(self):
        """Test case for get_build_logs

        """
        pass

    def test_get_builds(self):
        """Test case for get_builds

        """
        pass

    def test_get_org_builds(self):
        """Test case for get_org_builds

        """
        pass

    def test_restart_build(self):
        """Test case for restart_build

        """
        pass

    def test_update_build(self):
        """Test case for update_build

        """
        pass


if __name__ == '__main__':
    unittest.main()
