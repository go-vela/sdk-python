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

class Container(object):
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
        'commands': 'list[str]',
        'detach': 'bool',
        'directory': 'str',
        'entrypoint': 'list[str]',
        'environment': 'dict(str, str)',
        'exit_code': 'int',
        'id': 'str',
        'image': 'str',
        'name': 'str',
        'needs': 'list[str]',
        'networks': 'list[str]',
        'number': 'int',
        'ports': 'list[str]',
        'privileged': 'bool',
        'pull': 'str',
        'ruleset': 'Ruleset',
        'secrets': 'StepSecretSlice',
        'ulimits': 'UlimitSlice',
        'volumes': 'VolumeSlice'
    }

    attribute_map = {
        'commands': 'commands',
        'detach': 'detach',
        'directory': 'directory',
        'entrypoint': 'entrypoint',
        'environment': 'environment',
        'exit_code': 'exit_code',
        'id': 'id',
        'image': 'image',
        'name': 'name',
        'needs': 'needs',
        'networks': 'networks',
        'number': 'number',
        'ports': 'ports',
        'privileged': 'privileged',
        'pull': 'pull',
        'ruleset': 'ruleset',
        'secrets': 'secrets',
        'ulimits': 'ulimits',
        'volumes': 'volumes'
    }

    def __init__(self, commands=None, detach=None, directory=None, entrypoint=None, environment=None, exit_code=None, id=None, image=None, name=None, needs=None, networks=None, number=None, ports=None, privileged=None, pull=None, ruleset=None, secrets=None, ulimits=None, volumes=None):  # noqa: E501
        """Container - a model defined in Swagger"""  # noqa: E501
        self._commands = None
        self._detach = None
        self._directory = None
        self._entrypoint = None
        self._environment = None
        self._exit_code = None
        self._id = None
        self._image = None
        self._name = None
        self._needs = None
        self._networks = None
        self._number = None
        self._ports = None
        self._privileged = None
        self._pull = None
        self._ruleset = None
        self._secrets = None
        self._ulimits = None
        self._volumes = None
        self.discriminator = None
        if commands is not None:
            self.commands = commands
        if detach is not None:
            self.detach = detach
        if directory is not None:
            self.directory = directory
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if environment is not None:
            self.environment = environment
        if exit_code is not None:
            self.exit_code = exit_code
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if name is not None:
            self.name = name
        if needs is not None:
            self.needs = needs
        if networks is not None:
            self.networks = networks
        if number is not None:
            self.number = number
        if ports is not None:
            self.ports = ports
        if privileged is not None:
            self.privileged = privileged
        if pull is not None:
            self.pull = pull
        if ruleset is not None:
            self.ruleset = ruleset
        if secrets is not None:
            self.secrets = secrets
        if ulimits is not None:
            self.ulimits = ulimits
        if volumes is not None:
            self.volumes = volumes

    @property
    def commands(self):
        """Gets the commands of this Container.  # noqa: E501


        :return: The commands of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this Container.


        :param commands: The commands of this Container.  # noqa: E501
        :type: list[str]
        """

        self._commands = commands

    @property
    def detach(self):
        """Gets the detach of this Container.  # noqa: E501


        :return: The detach of this Container.  # noqa: E501
        :rtype: bool
        """
        return self._detach

    @detach.setter
    def detach(self, detach):
        """Sets the detach of this Container.


        :param detach: The detach of this Container.  # noqa: E501
        :type: bool
        """

        self._detach = detach

    @property
    def directory(self):
        """Gets the directory of this Container.  # noqa: E501


        :return: The directory of this Container.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this Container.


        :param directory: The directory of this Container.  # noqa: E501
        :type: str
        """

        self._directory = directory

    @property
    def entrypoint(self):
        """Gets the entrypoint of this Container.  # noqa: E501


        :return: The entrypoint of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this Container.


        :param entrypoint: The entrypoint of this Container.  # noqa: E501
        :type: list[str]
        """

        self._entrypoint = entrypoint

    @property
    def environment(self):
        """Gets the environment of this Container.  # noqa: E501


        :return: The environment of this Container.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Container.


        :param environment: The environment of this Container.  # noqa: E501
        :type: dict(str, str)
        """

        self._environment = environment

    @property
    def exit_code(self):
        """Gets the exit_code of this Container.  # noqa: E501


        :return: The exit_code of this Container.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this Container.


        :param exit_code: The exit_code of this Container.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def id(self):
        """Gets the id of this Container.  # noqa: E501


        :return: The id of this Container.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Container.


        :param id: The id of this Container.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this Container.  # noqa: E501


        :return: The image of this Container.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Container.


        :param image: The image of this Container.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this Container.  # noqa: E501


        :return: The name of this Container.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Container.


        :param name: The name of this Container.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def needs(self):
        """Gets the needs of this Container.  # noqa: E501


        :return: The needs of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._needs

    @needs.setter
    def needs(self, needs):
        """Sets the needs of this Container.


        :param needs: The needs of this Container.  # noqa: E501
        :type: list[str]
        """

        self._needs = needs

    @property
    def networks(self):
        """Gets the networks of this Container.  # noqa: E501


        :return: The networks of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this Container.


        :param networks: The networks of this Container.  # noqa: E501
        :type: list[str]
        """

        self._networks = networks

    @property
    def number(self):
        """Gets the number of this Container.  # noqa: E501


        :return: The number of this Container.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Container.


        :param number: The number of this Container.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def ports(self):
        """Gets the ports of this Container.  # noqa: E501


        :return: The ports of this Container.  # noqa: E501
        :rtype: list[str]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Container.


        :param ports: The ports of this Container.  # noqa: E501
        :type: list[str]
        """

        self._ports = ports

    @property
    def privileged(self):
        """Gets the privileged of this Container.  # noqa: E501


        :return: The privileged of this Container.  # noqa: E501
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this Container.


        :param privileged: The privileged of this Container.  # noqa: E501
        :type: bool
        """

        self._privileged = privileged

    @property
    def pull(self):
        """Gets the pull of this Container.  # noqa: E501


        :return: The pull of this Container.  # noqa: E501
        :rtype: str
        """
        return self._pull

    @pull.setter
    def pull(self, pull):
        """Sets the pull of this Container.


        :param pull: The pull of this Container.  # noqa: E501
        :type: str
        """

        self._pull = pull

    @property
    def ruleset(self):
        """Gets the ruleset of this Container.  # noqa: E501


        :return: The ruleset of this Container.  # noqa: E501
        :rtype: Ruleset
        """
        return self._ruleset

    @ruleset.setter
    def ruleset(self, ruleset):
        """Sets the ruleset of this Container.


        :param ruleset: The ruleset of this Container.  # noqa: E501
        :type: Ruleset
        """

        self._ruleset = ruleset

    @property
    def secrets(self):
        """Gets the secrets of this Container.  # noqa: E501


        :return: The secrets of this Container.  # noqa: E501
        :rtype: StepSecretSlice
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this Container.


        :param secrets: The secrets of this Container.  # noqa: E501
        :type: StepSecretSlice
        """

        self._secrets = secrets

    @property
    def ulimits(self):
        """Gets the ulimits of this Container.  # noqa: E501


        :return: The ulimits of this Container.  # noqa: E501
        :rtype: UlimitSlice
        """
        return self._ulimits

    @ulimits.setter
    def ulimits(self, ulimits):
        """Sets the ulimits of this Container.


        :param ulimits: The ulimits of this Container.  # noqa: E501
        :type: UlimitSlice
        """

        self._ulimits = ulimits

    @property
    def volumes(self):
        """Gets the volumes of this Container.  # noqa: E501


        :return: The volumes of this Container.  # noqa: E501
        :rtype: VolumeSlice
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Container.


        :param volumes: The volumes of this Container.  # noqa: E501
        :type: VolumeSlice
        """

        self._volumes = volumes

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
        if issubclass(Container, dict):
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
        if not isinstance(other, Container):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
