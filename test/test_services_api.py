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
from vela.vela.services_api import ServicesApi  # noqa: E501
from vela.rest import ApiException


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self):
        self.api = ServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service(self):
        """Test case for create_service

        """
        pass

    def test_create_service_logs(self):
        """Test case for create_service_logs

        """
        pass

    def test_delete_service(self):
        """Test case for delete_service

        """
        pass

    def test_delete_service_logs(self):
        """Test case for delete_service_logs

        """
        pass

    def test_get_service(self):
        """Test case for get_service

        """
        pass

    def test_get_service_logs(self):
        """Test case for get_service_logs

        """
        pass

    def test_get_services(self):
        """Test case for get_services

        """
        pass

    def test_update_service(self):
        """Test case for update_service

        """
        pass

    def test_update_service_log(self):
        """Test case for update_service_log

        """
        pass


if __name__ == '__main__':
    unittest.main()
