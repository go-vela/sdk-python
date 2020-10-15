# coding: utf-8
#
# Copyright (c) 2020 Target Brands, Inc. All rights reserved.

"""
    Vela server

    API for the Vela server  # noqa: E501

    OpenAPI spec version: 0.4.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vela.api_client import ApiClient


class ReposApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def chown_repo(self, repo, org, **kwargs):  # noqa: E501
        """chown_repo  # noqa: E501

        Remove and recreate the webhook for a repo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chown_repo(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.chown_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.chown_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def chown_repo_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """chown_repo  # noqa: E501

        Remove and recreate the webhook for a repo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.chown_repo_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chown_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `chown_repo`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `chown_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

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
            '/api/v1/repos/{org}/{repo}/chown', 'PATCH',
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

    def create_repo(self, body, **kwargs):  # noqa: E501
        """create_repo  # noqa: E501

        Create a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_repo(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Repo body: Payload containing the repo to create (required)
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_repo_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_repo_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_repo_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_repo  # noqa: E501

        Create a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_repo_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Repo body: Payload containing the repo to create (required)
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/api/v1/repos', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Repo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_repo(self, repo, org, **kwargs):  # noqa: E501
        """delete_repo  # noqa: E501

        Delete a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repo(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def delete_repo_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """delete_repo  # noqa: E501

        Delete a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_repo_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `delete_repo`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `delete_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

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
            '/api/v1/repos/{org}/{repo}', 'DELETE',
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

    def get_repo(self, repo, org, **kwargs):  # noqa: E501
        """get_repo  # noqa: E501

        Get a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repo(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.get_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def get_repo_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """get_repo  # noqa: E501

        Get a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repo_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `get_repo`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

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
            '/api/v1/repos/{org}/{repo}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Repo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_repos(self, **kwargs):  # noqa: E501
        """get_repos  # noqa: E501

        Get all repos in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repos(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_repos_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_repos_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_repos_with_http_info(self, **kwargs):  # noqa: E501
        """get_repos  # noqa: E501

        Get all repos in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_repos_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_repos" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/v1/repos', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Repo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def repair_repo(self, repo, org, **kwargs):  # noqa: E501
        """repair_repo  # noqa: E501

        Remove and recreate the webhook for a repo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repair_repo(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.repair_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.repair_repo_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def repair_repo_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """repair_repo  # noqa: E501

        Remove and recreate the webhook for a repo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.repair_repo_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method repair_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `repair_repo`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `repair_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

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
            '/api/v1/repos/{org}/{repo}/repair', 'DELETE',
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

    def update_repo(self, body, repo, org, **kwargs):  # noqa: E501
        """update_repo  # noqa: E501

        Update a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repo(body, repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Repo body: Payload containing the repo to update (required)
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_repo_with_http_info(body, repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.update_repo_with_http_info(body, repo, org, **kwargs)  # noqa: E501
            return data

    def update_repo_with_http_info(self, body, repo, org, **kwargs):  # noqa: E501
        """update_repo  # noqa: E501

        Update a repo in the configured backend  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_repo_with_http_info(body, repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Repo body: Payload containing the repo to update (required)
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :return: Repo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'repo', 'org']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_repo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_repo`")  # noqa: E501
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `update_repo`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `update_repo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

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
            '/api/v1/repos/{org}/{repo}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Repo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
