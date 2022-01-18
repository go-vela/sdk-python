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


class SecretsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_secret(self, body, engine, type, org, name, **kwargs):  # noqa: E501
        """create_secret  # noqa: E501

        Create a secret  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_secret(body, engine, type, org, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Secret body: Payload containing the secret to create (required)
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :return: Secret
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_secret_with_http_info(body, engine, type, org, name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_secret_with_http_info(body, engine, type, org, name, **kwargs)  # noqa: E501
            return data

    def create_secret_with_http_info(self, body, engine, type, org, name, **kwargs):  # noqa: E501
        """create_secret  # noqa: E501

        Create a secret  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_secret_with_http_info(body, engine, type, org, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Secret body: Payload containing the secret to create (required)
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :return: Secret
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'engine', 'type', 'org', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_secret`")  # noqa: E501
        # verify the required parameter 'engine' is set
        if ('engine' not in params or
                params['engine'] is None):
            raise ValueError("Missing the required parameter `engine` when calling `create_secret`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `create_secret`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `create_secret`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'engine' in params:
            path_params['engine'] = params['engine']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/api/v1/secrets/{engine}/{type}/{org}/{name}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Secret',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_secret(self, body, engine, type, org, name, secret, **kwargs):  # noqa: E501
        """Delete a secret from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_secret(body, engine, type, org, name, secret, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Secret body: Payload containing secret to update (required)
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :param str secret: Name of the secret (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_secret_with_http_info(body, engine, type, org, name, secret, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_secret_with_http_info(body, engine, type, org, name, secret, **kwargs)  # noqa: E501
            return data

    def delete_secret_with_http_info(self, body, engine, type, org, name, secret, **kwargs):  # noqa: E501
        """Delete a secret from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_secret_with_http_info(body, engine, type, org, name, secret, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Secret body: Payload containing secret to update (required)
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :param str secret: Name of the secret (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'engine', 'type', 'org', 'name', 'secret']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_secret`")  # noqa: E501
        # verify the required parameter 'engine' is set
        if ('engine' not in params or
                params['engine'] is None):
            raise ValueError("Missing the required parameter `engine` when calling `delete_secret`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `delete_secret`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `delete_secret`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_secret`")  # noqa: E501
        # verify the required parameter 'secret' is set
        if ('secret' not in params or
                params['secret'] is None):
            raise ValueError("Missing the required parameter `secret` when calling `delete_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'engine' in params:
            path_params['engine'] = params['engine']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'secret' in params:
            path_params['secret'] = params['secret']  # noqa: E501

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
            '/api/v1/secrets/{engine}/{type}/{org}/{name}/{secret}', 'DELETE',
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

    def get_secret(self, engine, type, org, name, secret, **kwargs):  # noqa: E501
        """Retrieve a secret from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_secret(engine, type, org, name, secret, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :param str secret: Name of the secret (required)
        :return: Secret
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_secret_with_http_info(engine, type, org, name, secret, **kwargs)  # noqa: E501
        else:
            (data) = self.get_secret_with_http_info(engine, type, org, name, secret, **kwargs)  # noqa: E501
            return data

    def get_secret_with_http_info(self, engine, type, org, name, secret, **kwargs):  # noqa: E501
        """Retrieve a secret from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_secret_with_http_info(engine, type, org, name, secret, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :param str secret: Name of the secret (required)
        :return: Secret
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['engine', 'type', 'org', 'name', 'secret']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_secret" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'engine' is set
        if ('engine' not in params or
                params['engine'] is None):
            raise ValueError("Missing the required parameter `engine` when calling `get_secret`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_secret`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_secret`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_secret`")  # noqa: E501
        # verify the required parameter 'secret' is set
        if ('secret' not in params or
                params['secret'] is None):
            raise ValueError("Missing the required parameter `secret` when calling `get_secret`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'engine' in params:
            path_params['engine'] = params['engine']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'secret' in params:
            path_params['secret'] = params['secret']  # noqa: E501

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
            '/api/v1/secrets/{engine}/{type}/{org}/{name}/{secret}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Secret',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_secrets(self, engine, type, org, name, **kwargs):  # noqa: E501
        """Retrieve a list of secrets from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_secrets(engine, type, org, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :return: list[Secret]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_secrets_with_http_info(engine, type, org, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_secrets_with_http_info(engine, type, org, name, **kwargs)  # noqa: E501
            return data

    def get_secrets_with_http_info(self, engine, type, org, name, **kwargs):  # noqa: E501
        """Retrieve a list of secrets from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_secrets_with_http_info(engine, type, org, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :return: list[Secret]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['engine', 'type', 'org', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_secrets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'engine' is set
        if ('engine' not in params or
                params['engine'] is None):
            raise ValueError("Missing the required parameter `engine` when calling `get_secrets`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_secrets`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `get_secrets`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_secrets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'engine' in params:
            path_params['engine'] = params['engine']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/api/v1/secrets/{engine}/{type}/{org}/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Secret]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_secrets(self, body, engine, type, org, name, secret, **kwargs):  # noqa: E501
        """Update a secret from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_secrets(body, engine, type, org, name, secret, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Secret body: Payload containing the secret to create (required)
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :param str secret: Name of the secret (required)
        :return: Secret
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_secrets_with_http_info(body, engine, type, org, name, secret, **kwargs)  # noqa: E501
        else:
            (data) = self.update_secrets_with_http_info(body, engine, type, org, name, secret, **kwargs)  # noqa: E501
            return data

    def update_secrets_with_http_info(self, body, engine, type, org, name, secret, **kwargs):  # noqa: E501
        """Update a secret from the configured backend.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_secrets_with_http_info(body, engine, type, org, name, secret, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Secret body: Payload containing the secret to create (required)
        :param str engine: Secret engine to create a secret in (required)
        :param str type: Secret type to create. Options 'org', 'repo', or 'shared' (required)
        :param str org: Name of the org (required)
        :param str name: Name of the repo if a repo secret, team name if a shared secret, or '*' if an org secret (required)
        :param str secret: Name of the secret (required)
        :return: Secret
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'engine', 'type', 'org', 'name', 'secret']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_secrets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_secrets`")  # noqa: E501
        # verify the required parameter 'engine' is set
        if ('engine' not in params or
                params['engine'] is None):
            raise ValueError("Missing the required parameter `engine` when calling `update_secrets`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `update_secrets`")  # noqa: E501
        # verify the required parameter 'org' is set
        if ('org' not in params or
                params['org'] is None):
            raise ValueError("Missing the required parameter `org` when calling `update_secrets`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update_secrets`")  # noqa: E501
        # verify the required parameter 'secret' is set
        if ('secret' not in params or
                params['secret'] is None):
            raise ValueError("Missing the required parameter `secret` when calling `update_secrets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'engine' in params:
            path_params['engine'] = params['engine']  # noqa: E501
        if 'type' in params:
            path_params['type'] = params['type']  # noqa: E501
        if 'org' in params:
            path_params['org'] = params['org']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501
        if 'secret' in params:
            path_params['secret'] = params['secret']  # noqa: E501

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
            '/api/v1/secrets/{engine}/{type}/{org}/{name}/{secret}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Secret',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
