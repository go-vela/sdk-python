# coding: utf-8
#
# Copyright (c) 2021 Target Brands, Inc. All rights reserved.

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Executor(object):
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
        'build': 'Build',
        'distribution': 'str',
        'host': 'str',
        'id': 'int',
        'pipeline': 'PipelineBuild',
        'repo': 'Repo',
        'runtime': 'str'
    }

    attribute_map = {
        'build': 'build',
        'distribution': 'distribution',
        'host': 'host',
        'id': 'id',
        'pipeline': 'pipeline',
        'repo': 'repo',
        'runtime': 'runtime'
    }

    def __init__(self, build=None, distribution=None, host=None, id=None, pipeline=None, repo=None, runtime=None):  # noqa: E501
        """Executor - a model defined in Swagger"""  # noqa: E501
        self._build = None
        self._distribution = None
        self._host = None
        self._id = None
        self._pipeline = None
        self._repo = None
        self._runtime = None
        self.discriminator = None
        if build is not None:
            self.build = build
        if distribution is not None:
            self.distribution = distribution
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if pipeline is not None:
            self.pipeline = pipeline
        if repo is not None:
            self.repo = repo
        if runtime is not None:
            self.runtime = runtime

    @property
    def build(self):
        """Gets the build of this Executor.  # noqa: E501


        :return: The build of this Executor.  # noqa: E501
        :rtype: Build
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this Executor.


        :param build: The build of this Executor.  # noqa: E501
        :type: Build
        """

        self._build = build

    @property
    def distribution(self):
        """Gets the distribution of this Executor.  # noqa: E501


        :return: The distribution of this Executor.  # noqa: E501
        :rtype: str
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this Executor.


        :param distribution: The distribution of this Executor.  # noqa: E501
        :type: str
        """

        self._distribution = distribution

    @property
    def host(self):
        """Gets the host of this Executor.  # noqa: E501


        :return: The host of this Executor.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Executor.


        :param host: The host of this Executor.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this Executor.  # noqa: E501


        :return: The id of this Executor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Executor.


        :param id: The id of this Executor.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pipeline(self):
        """Gets the pipeline of this Executor.  # noqa: E501


        :return: The pipeline of this Executor.  # noqa: E501
        :rtype: PipelineBuild
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """Sets the pipeline of this Executor.


        :param pipeline: The pipeline of this Executor.  # noqa: E501
        :type: PipelineBuild
        """

        self._pipeline = pipeline

    @property
    def repo(self):
        """Gets the repo of this Executor.  # noqa: E501


        :return: The repo of this Executor.  # noqa: E501
        :rtype: Repo
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this Executor.


        :param repo: The repo of this Executor.  # noqa: E501
        :type: Repo
        """

        self._repo = repo

    @property
    def runtime(self):
        """Gets the runtime of this Executor.  # noqa: E501


        :return: The runtime of this Executor.  # noqa: E501
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this Executor.


        :param runtime: The runtime of this Executor.  # noqa: E501
        :type: str
        """

        self._runtime = runtime

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
        if issubclass(Executor, dict):
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
        if not isinstance(other, Executor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
