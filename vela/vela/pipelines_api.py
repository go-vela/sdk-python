# coding: utf-8
#
# Copyright (c) 2021 Target Brands, Inc. All rights reserved.

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


class PipelinesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def compile_pipeline(self, repo, org, **kwargs):  # noqa: E501
        """compile_pipeline  # noqa: E501

        Get, expand and compile a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compile_pipeline(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: PipelineBuild
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.compile_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.compile_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def compile_pipeline_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """compile_pipeline  # noqa: E501

        Get, expand and compile a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compile_pipeline_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: PipelineBuild
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org', 'ref', 'output']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compile_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `compile_pipeline`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `compile_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

        query_params = []
        if 'ref' in params:
            query_params.append(('ref', params['ref']))  # noqa: E501
        if 'output' in params:
            query_params.append(('output', params['output']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-yaml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipelines/{org}/{repo}/compile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PipelineBuild',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def expand_pipeline(self, repo, org, **kwargs):  # noqa: E501
        """expand_pipeline  # noqa: E501

        Get and expand a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.expand_pipeline(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: PipelineBuild
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.expand_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.expand_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def expand_pipeline_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """expand_pipeline  # noqa: E501

        Get and expand a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.expand_pipeline_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: PipelineBuild
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org', 'ref', 'output']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method expand_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `expand_pipeline`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `expand_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

        query_params = []
        if 'ref' in params:
            query_params.append(('ref', params['ref']))  # noqa: E501
        if 'output' in params:
            query_params.append(('output', params['output']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-yaml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipelines/{org}/{repo}/expand', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PipelineBuild',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pipeline(self, repo, org, **kwargs):  # noqa: E501
        """get_pipeline  # noqa: E501

        Get a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: PipelineBuild
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def get_pipeline_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """get_pipeline  # noqa: E501

        Get a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pipeline_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: PipelineBuild
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org', 'ref', 'output']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `get_pipeline`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

        query_params = []
        if 'ref' in params:
            query_params.append(('ref', params['ref']))  # noqa: E501
        if 'output' in params:
            query_params.append(('output', params['output']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-yaml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipelines/{org}/{repo}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PipelineBuild',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_templates(self, repo, org, **kwargs):  # noqa: E501
        """get_templates  # noqa: E501

        Get a map of templates utilized by a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_templates_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.get_templates_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def get_templates_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """get_templates  # noqa: E501

        Get a map of templates utilized by a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_templates_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: Template
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org', 'ref', 'output']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `get_templates`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

        query_params = []
        if 'ref' in params:
            query_params.append(('ref', params['ref']))  # noqa: E501
        if 'output' in params:
            query_params.append(('output', params['output']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/x-yaml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/pipelines/{org}/{repo}/templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Template',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_pipeline(self, repo, org, **kwargs):  # noqa: E501
        """validate_pipeline  # noqa: E501

        Get, expand and validate a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_pipeline(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_pipeline_with_http_info(repo, org, **kwargs)  # noqa: E501
            return data

    def validate_pipeline_with_http_info(self, repo, org, **kwargs):  # noqa: E501
        """validate_pipeline  # noqa: E501

        Get, expand and validate a pipeline configuration from the source provider  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_pipeline_with_http_info(repo, org, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str repo: Name of the repo (required)
        :param str org: Name of the org (required)
        :param str ref: Ref for retrieving pipeline configuration file
        :param str output: Output string for specifying output format
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['repo', 'org', 'ref', 'output']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_pipeline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'repo' is set
        if ('repo' not in params or
                params['repo'] is None):
            raise ValueError("Missing the required parameter `repo` when calling `validate_pipeline`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `validate_pipeline`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'repo' in params:
            path_params['repo'] = params['repo']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501

        query_params = []
        if 'ref' in params:
            query_params.append(('ref', params['ref']))  # noqa: E501
        if 'output' in params:
            query_params.append(('output', params['output']))  # noqa: E501

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
            '/api/v1/pipelines/{org}/{repo}/validate', 'POST',
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
