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

class Log(object):
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
        'build_id': 'int',
        'data': 'str',
        'id': 'int',
        'repo_id': 'int',
        'service_id': 'int',
        'step_id': 'int'
    }

    attribute_map = {
        'build_id': 'build_id',
        'data': 'data',
        'id': 'id',
        'repo_id': 'repo_id',
        'service_id': 'service_id',
        'step_id': 'step_id'
    }

    def __init__(self, build_id=None, data=None, id=None, repo_id=None, service_id=None, step_id=None):  # noqa: E501
        """Log - a model defined in Swagger"""  # noqa: E501
        self._build_id = None
        self._data = None
        self._id = None
        self._repo_id = None
        self._service_id = None
        self._step_id = None
        self.discriminator = None
        if build_id is not None:
            self.build_id = build_id
        if data is not None:
            self.data = data
        if id is not None:
            self.id = id
        if repo_id is not None:
            self.repo_id = repo_id
        if service_id is not None:
            self.service_id = service_id
        if step_id is not None:
            self.step_id = step_id

    @property
    def build_id(self):
        """Gets the build_id of this Log.  # noqa: E501


        :return: The build_id of this Log.  # noqa: E501
        :rtype: int
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this Log.


        :param build_id: The build_id of this Log.  # noqa: E501
        :type: int
        """

        self._build_id = build_id

    @property
    def data(self):
        """Gets the data of this Log.  # noqa: E501


        :return: The data of this Log.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Log.


        :param data: The data of this Log.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def id(self):
        """Gets the id of this Log.  # noqa: E501


        :return: The id of this Log.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Log.


        :param id: The id of this Log.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def repo_id(self):
        """Gets the repo_id of this Log.  # noqa: E501


        :return: The repo_id of this Log.  # noqa: E501
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this Log.


        :param repo_id: The repo_id of this Log.  # noqa: E501
        :type: int
        """

        self._repo_id = repo_id

    @property
    def service_id(self):
        """Gets the service_id of this Log.  # noqa: E501


        :return: The service_id of this Log.  # noqa: E501
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this Log.


        :param service_id: The service_id of this Log.  # noqa: E501
        :type: int
        """

        self._service_id = service_id

    @property
    def step_id(self):
        """Gets the step_id of this Log.  # noqa: E501


        :return: The step_id of this Log.  # noqa: E501
        :rtype: int
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        """Sets the step_id of this Log.


        :param step_id: The step_id of this Log.  # noqa: E501
        :type: int
        """

        self._step_id = step_id

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
        if issubclass(Log, dict):
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
        if not isinstance(other, Log):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
