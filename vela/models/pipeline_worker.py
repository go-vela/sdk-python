# coding: utf-8
#
# Copyright (c) 2020 Target Brands, Inc. All rights reserved.

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PipelineWorker(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'flavor': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'flavor': 'flavor',
        'platform': 'platform'
    }

    def __init__(self, flavor=None, platform=None):  # noqa: E501
        """PipelineWorker - a model defined in Swagger"""  # noqa: E501
        self._flavor = None
        self._platform = None
        self.discriminator = None
        if flavor is not None:
            self.flavor = flavor
        if platform is not None:
            self.platform = platform

    @property
    def flavor(self):
        """Gets the flavor of this PipelineWorker.  # noqa: E501


        :return: The flavor of this PipelineWorker.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this PipelineWorker.


        :param flavor: The flavor of this PipelineWorker.  # noqa: E501
        :type: str
        """

        self._flavor = flavor

    @property
    def platform(self):
        """Gets the platform of this PipelineWorker.  # noqa: E501


        :return: The platform of this PipelineWorker.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PipelineWorker.


        :param platform: The platform of this PipelineWorker.  # noqa: E501
        :type: str
        """

        self._platform = platform

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PipelineWorker, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PipelineWorker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other