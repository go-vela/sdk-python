# coding: utf-8

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.4.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Step(object):
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
        'created': 'int',
        'distribution': 'str',
        'error': 'str',
        'exit_code': 'int',
        'finished': 'int',
        'host': 'str',
        'id': 'int',
        'image': 'str',
        'name': 'str',
        'number': 'int',
        'repo_id': 'int',
        'runtime': 'str',
        'stage': 'str',
        'started': 'int',
        'status': 'str'
    }

    attribute_map = {
        'build_id': 'build_id',
        'created': 'created',
        'distribution': 'distribution',
        'error': 'error',
        'exit_code': 'exit_code',
        'finished': 'finished',
        'host': 'host',
        'id': 'id',
        'image': 'image',
        'name': 'name',
        'number': 'number',
        'repo_id': 'repo_id',
        'runtime': 'runtime',
        'stage': 'stage',
        'started': 'started',
        'status': 'status'
    }

    def __init__(self, build_id=None, created=None, distribution=None, error=None, exit_code=None, finished=None, host=None, id=None, image=None, name=None, number=None, repo_id=None, runtime=None, stage=None, started=None, status=None):  # noqa: E501
        """Step - a model defined in Swagger"""  # noqa: E501
        self._build_id = None
        self._created = None
        self._distribution = None
        self._error = None
        self._exit_code = None
        self._finished = None
        self._host = None
        self._id = None
        self._image = None
        self._name = None
        self._number = None
        self._repo_id = None
        self._runtime = None
        self._stage = None
        self._started = None
        self._status = None
        self.discriminator = None
        if build_id is not None:
            self.build_id = build_id
        if created is not None:
            self.created = created
        if distribution is not None:
            self.distribution = distribution
        if error is not None:
            self.error = error
        if exit_code is not None:
            self.exit_code = exit_code
        if finished is not None:
            self.finished = finished
        if host is not None:
            self.host = host
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if repo_id is not None:
            self.repo_id = repo_id
        if runtime is not None:
            self.runtime = runtime
        if stage is not None:
            self.stage = stage
        if started is not None:
            self.started = started
        if status is not None:
            self.status = status

    @property
    def build_id(self):
        """Gets the build_id of this Step.  # noqa: E501


        :return: The build_id of this Step.  # noqa: E501
        :rtype: int
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this Step.


        :param build_id: The build_id of this Step.  # noqa: E501
        :type: int
        """

        self._build_id = build_id

    @property
    def created(self):
        """Gets the created of this Step.  # noqa: E501


        :return: The created of this Step.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Step.


        :param created: The created of this Step.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def distribution(self):
        """Gets the distribution of this Step.  # noqa: E501


        :return: The distribution of this Step.  # noqa: E501
        :rtype: str
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this Step.


        :param distribution: The distribution of this Step.  # noqa: E501
        :type: str
        """

        self._distribution = distribution

    @property
    def error(self):
        """Gets the error of this Step.  # noqa: E501


        :return: The error of this Step.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Step.


        :param error: The error of this Step.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def exit_code(self):
        """Gets the exit_code of this Step.  # noqa: E501


        :return: The exit_code of this Step.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this Step.


        :param exit_code: The exit_code of this Step.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def finished(self):
        """Gets the finished of this Step.  # noqa: E501


        :return: The finished of this Step.  # noqa: E501
        :rtype: int
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this Step.


        :param finished: The finished of this Step.  # noqa: E501
        :type: int
        """

        self._finished = finished

    @property
    def host(self):
        """Gets the host of this Step.  # noqa: E501


        :return: The host of this Step.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Step.


        :param host: The host of this Step.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def id(self):
        """Gets the id of this Step.  # noqa: E501


        :return: The id of this Step.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Step.


        :param id: The id of this Step.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this Step.  # noqa: E501


        :return: The image of this Step.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Step.


        :param image: The image of this Step.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this Step.  # noqa: E501


        :return: The name of this Step.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Step.


        :param name: The name of this Step.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this Step.  # noqa: E501


        :return: The number of this Step.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Step.


        :param number: The number of this Step.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def repo_id(self):
        """Gets the repo_id of this Step.  # noqa: E501


        :return: The repo_id of this Step.  # noqa: E501
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this Step.


        :param repo_id: The repo_id of this Step.  # noqa: E501
        :type: int
        """

        self._repo_id = repo_id

    @property
    def runtime(self):
        """Gets the runtime of this Step.  # noqa: E501


        :return: The runtime of this Step.  # noqa: E501
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this Step.


        :param runtime: The runtime of this Step.  # noqa: E501
        :type: str
        """

        self._runtime = runtime

    @property
    def stage(self):
        """Gets the stage of this Step.  # noqa: E501


        :return: The stage of this Step.  # noqa: E501
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this Step.


        :param stage: The stage of this Step.  # noqa: E501
        :type: str
        """

        self._stage = stage

    @property
    def started(self):
        """Gets the started of this Step.  # noqa: E501


        :return: The started of this Step.  # noqa: E501
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this Step.


        :param started: The started of this Step.  # noqa: E501
        :type: int
        """

        self._started = started

    @property
    def status(self):
        """Gets the status of this Step.  # noqa: E501


        :return: The status of this Step.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Step.


        :param status: The status of this Step.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(Step, dict):
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
        if not isinstance(other, Step):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
