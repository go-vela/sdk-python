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

class Volume(object):
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
        'access_mode': 'str',
        'destination': 'str',
        'source': 'str'
    }

    attribute_map = {
        'access_mode': 'access_mode',
        'destination': 'destination',
        'source': 'source'
    }

    def __init__(self, access_mode=None, destination=None, source=None):  # noqa: E501
        """Volume - a model defined in Swagger"""  # noqa: E501
        self._access_mode = None
        self._destination = None
        self._source = None
        self.discriminator = None
        if access_mode is not None:
            self.access_mode = access_mode
        if destination is not None:
            self.destination = destination
        if source is not None:
            self.source = source

    @property
    def access_mode(self):
        """Gets the access_mode of this Volume.  # noqa: E501


        :return: The access_mode of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this Volume.


        :param access_mode: The access_mode of this Volume.  # noqa: E501
        :type: str
        """

        self._access_mode = access_mode

    @property
    def destination(self):
        """Gets the destination of this Volume.  # noqa: E501


        :return: The destination of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this Volume.


        :param destination: The destination of this Volume.  # noqa: E501
        :type: str
        """

        self._destination = destination

    @property
    def source(self):
        """Gets the source of this Volume.  # noqa: E501


        :return: The source of this Volume.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Volume.


        :param source: The source of this Volume.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if issubclass(Volume, dict):
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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other