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

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vela.api_client import ApiClient


class BuildsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_build(self, body, org, repo, **kwargs):  # noqa: E501
        """create_build  # noqa: E501

        Create a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_build(body, org, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Build body: Payload containing the build to update (required)
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_build_with_http_info(body, org, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.create_build_with_http_info(body, org, repo, **kwargs)  # noqa: E501
            return data

    def create_build_with_http_info(self, body, org, repo, **kwargs):  # noqa: E501
        """create_build  # noqa: E501

        Create a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_build_with_http_info(body, org, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Build body: Payload containing the build to update (required)
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'org', 'repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_build" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_build`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `create_build`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `create_build`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}/{repo}/builds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Build',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_build(self, org, repo, build, **kwargs):  # noqa: E501
        """delete_build  # noqa: E501

        Delete a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_build(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_build_with_http_info(org, repo, build, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_build_with_http_info(org, repo, build, **kwargs)  # noqa: E501
            return data

    def delete_build_with_http_info(self, org, repo, build, **kwargs):  # noqa: E501
        """delete_build  # noqa: E501

        Delete a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_build_with_http_info(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org', 'repo', 'build']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_build" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `delete_build`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `delete_build`")  # noqa: E501
        # verify the required parameter 'build' is set
        if ('build' not in params or
                params['build'] is None):
            raise ValueError("Missing the required parameter `build` when calling `delete_build`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'build' in params:
            path_params['build'] = params['build']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}/{repo}/builds/{build}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_build(self, org, repo, build, **kwargs):  # noqa: E501
        """get_build  # noqa: E501

        Get a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_build_with_http_info(org, repo, build, **kwargs)  # noqa: E501
        else:
            (data) = self.get_build_with_http_info(org, repo, build, **kwargs)  # noqa: E501
            return data

    def get_build_with_http_info(self, org, repo, build, **kwargs):  # noqa: E501
        """get_build  # noqa: E501

        Get a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_with_http_info(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org', 'repo', 'build']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_build" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_build`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `get_build`")  # noqa: E501
        # verify the required parameter 'build' is set
        if ('build' not in params or
                params['build'] is None):
            raise ValueError("Missing the required parameter `build` when calling `get_build`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'build' in params:
            path_params['build'] = params['build']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}/{repo}/builds/{build}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Build',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_build_logs(self, org, repo, build, **kwargs):  # noqa: E501
        """get_build_logs  # noqa: E501

        Get logs for a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_logs(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: list[Log]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_build_logs_with_http_info(org, repo, build, **kwargs)  # noqa: E501
        else:
            (data) = self.get_build_logs_with_http_info(org, repo, build, **kwargs)  # noqa: E501
            return data

    def get_build_logs_with_http_info(self, org, repo, build, **kwargs):  # noqa: E501
        """get_build_logs  # noqa: E501

        Get logs for a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_build_logs_with_http_info(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: list[Log]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org', 'repo', 'build']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_build_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_build_logs`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `get_build_logs`")  # noqa: E501
        # verify the required parameter 'build' is set
        if ('build' not in params or
                params['build'] is None):
            raise ValueError("Missing the required parameter `build` when calling `get_build_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'build' in params:
            path_params['build'] = params['build']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}/{repo}/builds/{build}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Log]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_builds(self, org, repo, **kwargs):  # noqa: E501
        """get_builds  # noqa: E501

        Create a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds(org, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :return: list[Build]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_builds_with_http_info(org, repo, **kwargs)  # noqa: E501
        else:
            (data) = self.get_builds_with_http_info(org, repo, **kwargs)  # noqa: E501
            return data

    def get_builds_with_http_info(self, org, repo, **kwargs):  # noqa: E501
        """get_builds  # noqa: E501

        Create a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_builds_with_http_info(org, repo, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :return: list[Build]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org', 'repo']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_builds" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_builds`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `get_builds`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}/{repo}/builds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Build]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_org_builds(self, org, authorization, **kwargs):  # noqa: E501
        """get_org_builds  # noqa: E501

        Get a list of builds by org in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_org_builds(org, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str authorization: Vela bearer token (required)
        :return: list[Build]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_org_builds_with_http_info(org, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_org_builds_with_http_info(org, authorization, **kwargs)  # noqa: E501
            return data

    def get_org_builds_with_http_info(self, org, authorization, **kwargs):  # noqa: E501
        """get_org_builds  # noqa: E501

        Get a list of builds by org in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_org_builds_with_http_info(org, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str authorization: Vela bearer token (required)
        :return: list[Build]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_org_builds" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_org_builds`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_org_builds`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Build]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def restart_build(self, org, repo, build, **kwargs):  # noqa: E501
        """restart_build  # noqa: E501

        Restart a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restart_build(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.restart_build_with_http_info(org, repo, build, **kwargs)  # noqa: E501
        else:
            (data) = self.restart_build_with_http_info(org, repo, build, **kwargs)  # noqa: E501
            return data

    def restart_build_with_http_info(self, org, repo, build, **kwargs):  # noqa: E501
        """restart_build  # noqa: E501

        Restart a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.restart_build_with_http_info(org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org', 'repo', 'build']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method restart_build" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `restart_build`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `restart_build`")  # noqa: E501
        # verify the required parameter 'build' is set
        if ('build' not in params or
                params['build'] is None):
            raise ValueError("Missing the required parameter `build` when calling `restart_build`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'build' in params:
            path_params['build'] = params['build']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}/{repo}/builds/{build}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Build',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_build(self, body, org, repo, build, **kwargs):  # noqa: E501
        """update_build  # noqa: E501

        Updates a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_build(body, org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Build body: Payload containing the build to update (required)
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_build_with_http_info(body, org, repo, build, **kwargs)  # noqa: E501
        else:
            (data) = self.update_build_with_http_info(body, org, repo, build, **kwargs)  # noqa: E501
            return data

    def update_build_with_http_info(self, body, org, repo, build, **kwargs):  # noqa: E501
        """update_build  # noqa: E501

        Updates a build in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_build_with_http_info(body, org, repo, build, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Build body: Payload containing the build to update (required)
        :param str org: Name of the org (required)
        :param str repo: Name of the repo (required)
        :param int build: Build number to restart (required)
        :return: Build
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'org', 'repo', 'build']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_build" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_build`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `update_build`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `update_build`")  # noqa: E501
        # verify the required parameter 'build' is set
        if ('build' not in params or
                params['build'] is None):
            raise ValueError("Missing the required parameter `build` when calling `update_build`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'build' in params:
            path_params['build'] = params['build']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/repos/{org}/{repo}/builds/{build}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Build',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
