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

class User(object):
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
        'active': 'bool',
        'admin': 'bool',
        'favorites': 'list[str]',
        'id': 'int',
        'name': 'str',
        'token': 'str'
    }

    attribute_map = {
        'active': 'active',
        'admin': 'admin',
        'favorites': 'favorites',
        'id': 'id',
        'name': 'name',
        'token': 'token'
    }

    def __init__(self, active=None, admin=None, favorites=None, id=None, name=None, token=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._admin = None
        self._favorites = None
        self._id = None
        self._name = None
        self._token = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if admin is not None:
            self.admin = admin
        if favorites is not None:
            self.favorites = favorites
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if token is not None:
            self.token = token

    @property
    def active(self):
        """Gets the active of this User.  # noqa: E501


        :return: The active of this User.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this User.


        :param active: The active of this User.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def admin(self):
        """Gets the admin of this User.  # noqa: E501


        :return: The admin of this User.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this User.


        :param admin: The admin of this User.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def favorites(self):
        """Gets the favorites of this User.  # noqa: E501


        :return: The favorites of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._favorites

    @favorites.setter
    def favorites(self, favorites):
        """Sets the favorites of this User.


        :param favorites: The favorites of this User.  # noqa: E501
        :type: list[str]
        """

        self._favorites = favorites

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def token(self):
        """Gets the token of this User.  # noqa: E501


        :return: The token of this User.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this User.


        :param token: The token of this User.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
