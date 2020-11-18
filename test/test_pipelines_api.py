# coding: utf-8
#
# Copyright (c) 2020 Target Brands, Inc. All rights reserved.

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import vela
from vela.vela.pipelines_api import PipelinesApi  # noqa: E501
from vela.rest import ApiException


class TestPipelinesApi(unittest.TestCase):
    """PipelinesApi unit test stubs"""

    def setUp(self):
        self.api = PipelinesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_compile_pipeline(self):
        """Test case for compile_pipeline

        """
        pass

    def test_expand_pipeline(self):
        """Test case for expand_pipeline

        """
        pass

    def test_get_pipeline(self):
        """Test case for get_pipeline

        """
        pass

    def test_get_templates(self):
        """Test case for get_templates

        """
        pass

    def test_validate_pipeline(self):
        """Test case for validate_pipeline

        """
        pass


if __name__ == '__main__':
    unittest.main()
