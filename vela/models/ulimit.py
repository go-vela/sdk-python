# coding: utf-8
#
# Copyright (c) 2022 Target Brands, Inc. All rights reserved.

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Ulimit(object):
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
        'hard': 'int',
        'name': 'str',
        'soft': 'int'
    }

    attribute_map = {
        'hard': 'hard',
        'name': 'name',
        'soft': 'soft'
    }

    def __init__(self, hard=None, name=None, soft=None):  # noqa: E501
        """Ulimit - a model defined in Swagger"""  # noqa: E501
        self._hard = None
        self._name = None
        self._soft = None
        self.discriminator = None
        if hard is not None:
            self.hard = hard
        if name is not None:
            self.name = name
        if soft is not None:
            self.soft = soft

    @property
    def hard(self):
        """Gets the hard of this Ulimit.  # noqa: E501


        :return: The hard of this Ulimit.  # noqa: E501
        :rtype: int
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """Sets the hard of this Ulimit.


        :param hard: The hard of this Ulimit.  # noqa: E501
        :type: int
        """

        self._hard = hard

    @property
    def name(self):
        """Gets the name of this Ulimit.  # noqa: E501


        :return: The name of this Ulimit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Ulimit.


        :param name: The name of this Ulimit.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def soft(self):
        """Gets the soft of this Ulimit.  # noqa: E501


        :return: The soft of this Ulimit.  # noqa: E501
        :rtype: int
        """
        return self._soft

    @soft.setter
    def soft(self, soft):
        """Sets the soft of this Ulimit.


        :param soft: The soft of this Ulimit.  # noqa: E501
        :type: int
        """

        self._soft = soft

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
        if issubclass(Ulimit, dict):
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
        if not isinstance(other, Ulimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
