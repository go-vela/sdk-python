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
from vela.vela.workers_api import WorkersApi  # noqa: E501
from vela.rest import ApiException


class TestWorkersApi(unittest.TestCase):
    """WorkersApi unit test stubs"""

    def setUp(self):
        self.api = WorkersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_worker(self):
        """Test case for create_worker

        """
        pass

    def test_delete_worker(self):
        """Test case for delete_worker

        """
        pass

    def test_get_worker(self):
        """Test case for get_worker

        """
        pass

    def test_get_workers(self):
        """Test case for get_workers

        """
        pass

    def test_update_worker(self):
        """Test case for update_worker

        """
        pass


if __name__ == '__main__':
    unittest.main()
