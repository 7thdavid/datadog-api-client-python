# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import re  # noqa: F401
import sys  # noqa: F401

from datadog_api_client.v2.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.v2.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from datadog_api_client.v2.model.api_error_response import APIErrorResponse
from datadog_api_client.v2.model.permissions_response import PermissionsResponse
from datadog_api_client.v2.model.query_sort_order import QuerySortOrder
from datadog_api_client.v2.model.service_account_create_request import ServiceAccountCreateRequest
from datadog_api_client.v2.model.user_create_request import UserCreateRequest
from datadog_api_client.v2.model.user_invitation_response import UserInvitationResponse
from datadog_api_client.v2.model.user_invitations_request import UserInvitationsRequest
from datadog_api_client.v2.model.user_invitations_response import UserInvitationsResponse
from datadog_api_client.v2.model.user_response import UserResponse
from datadog_api_client.v2.model.user_update_request import UserUpdateRequest
from datadog_api_client.v2.model.users_response import UsersResponse


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._create_service_account_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/service_accounts",
                "operation_id": "create_service_account",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (ServiceAccountCreateRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._create_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/users",
                "operation_id": "create_user",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (UserCreateRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._disable_user_endpoint = _Endpoint(
            settings={
                "response_type": None,
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/users/{user_id}",
                "operation_id": "disable_user",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "user_id",
                ],
                "required": [
                    "user_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user_id": (str,),
                },
                "attribute_map": {
                    "user_id": "user_id",
                },
                "location_map": {
                    "user_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_invitation_endpoint = _Endpoint(
            settings={
                "response_type": (UserInvitationResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/user_invitations/{user_invitation_uuid}",
                "operation_id": "get_invitation",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "user_invitation_uuid",
                ],
                "required": [
                    "user_invitation_uuid",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user_invitation_uuid": (str,),
                },
                "attribute_map": {
                    "user_invitation_uuid": "user_invitation_uuid",
                },
                "location_map": {
                    "user_invitation_uuid": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._get_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/users/{user_id}",
                "operation_id": "get_user",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "user_id",
                ],
                "required": [
                    "user_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user_id": (str,),
                },
                "attribute_map": {
                    "user_id": "user_id",
                },
                "location_map": {
                    "user_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_user_organizations_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/users/{user_id}/orgs",
                "operation_id": "list_user_organizations",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "user_id",
                ],
                "required": [
                    "user_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user_id": (str,),
                },
                "attribute_map": {
                    "user_id": "user_id",
                },
                "location_map": {
                    "user_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_user_permissions_endpoint = _Endpoint(
            settings={
                "response_type": (PermissionsResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/users/{user_id}/permissions",
                "operation_id": "list_user_permissions",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "user_id",
                ],
                "required": [
                    "user_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user_id": (str,),
                },
                "attribute_map": {
                    "user_id": "user_id",
                },
                "location_map": {
                    "user_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._list_users_endpoint = _Endpoint(
            settings={
                "response_type": (UsersResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/users",
                "operation_id": "list_users",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "page_size",
                    "page_number",
                    "sort",
                    "sort_dir",
                    "filter",
                    "filter_status",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "page_size": (int,),
                    "page_number": (int,),
                    "sort": (str,),
                    "sort_dir": (QuerySortOrder,),
                    "filter": (str,),
                    "filter_status": (str,),
                },
                "attribute_map": {
                    "page_size": "page[size]",
                    "page_number": "page[number]",
                    "sort": "sort",
                    "sort_dir": "sort_dir",
                    "filter": "filter",
                    "filter_status": "filter[status]",
                },
                "location_map": {
                    "page_size": "query",
                    "page_number": "query",
                    "sort": "query",
                    "sort_dir": "query",
                    "filter": "query",
                    "filter_status": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._send_invitations_endpoint = _Endpoint(
            settings={
                "response_type": (UserInvitationsResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/user_invitations",
                "operation_id": "send_invitations",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "body",
                ],
                "required": [
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "body": (UserInvitationsRequest,),
                },
                "attribute_map": {},
                "location_map": {
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

        self._update_user_endpoint = _Endpoint(
            settings={
                "response_type": (UserResponse,),
                "auth": ["AuthZ", "apiKeyAuth", "appKeyAuth"],
                "endpoint_path": "/api/v2/users/{user_id}",
                "operation_id": "update_user",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "user_id",
                    "body",
                ],
                "required": [
                    "user_id",
                    "body",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "user_id": (str,),
                    "body": (UserUpdateRequest,),
                },
                "attribute_map": {
                    "user_id": "user_id",
                },
                "location_map": {
                    "user_id": "path",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def create_service_account(self, body, **kwargs):
        """Create a service account  # noqa: E501

        Create a service account for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_service_account(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (ServiceAccountCreateRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_service_account_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_service_account_endpoint.call_with_http_info(**kwargs)

    def create_user(self, body, **kwargs):
        """Create a user  # noqa: E501

        Create a user for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (UserCreateRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._create_user_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._create_user_endpoint.call_with_http_info(**kwargs)

    def disable_user(self, user_id, **kwargs):
        """Disable a user  # noqa: E501

        Disable a user. Can only be used with an application key belonging to an administrator user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disable_user(user_id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str): The ID of the user.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._disable_user_endpoint.default_arguments(kwargs)
        kwargs["user_id"] = user_id
        return self._disable_user_endpoint.call_with_http_info(**kwargs)

    def get_invitation(self, user_invitation_uuid, **kwargs):
        """Get a user invitation  # noqa: E501

        Returns a single user invitation by its UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invitation(user_invitation_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            user_invitation_uuid (str): The UUID of the user invitation.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserInvitationResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_invitation_endpoint.default_arguments(kwargs)
        kwargs["user_invitation_uuid"] = user_invitation_uuid
        return self._get_invitation_endpoint.call_with_http_info(**kwargs)

    def get_user(self, user_id, **kwargs):
        """Get user details  # noqa: E501

        Get a user in the organization specified by the user’s `user_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user(user_id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str): The ID of the user.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._get_user_endpoint.default_arguments(kwargs)
        kwargs["user_id"] = user_id
        return self._get_user_endpoint.call_with_http_info(**kwargs)

    def list_user_organizations(self, user_id, **kwargs):
        """Get a user organization  # noqa: E501

        Get a user organization. Returns the user information and all organizations joined by this user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_user_organizations(user_id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str): The ID of the user.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_user_organizations_endpoint.default_arguments(kwargs)
        kwargs["user_id"] = user_id
        return self._list_user_organizations_endpoint.call_with_http_info(**kwargs)

    def list_user_permissions(self, user_id, **kwargs):
        """Get a user permissions  # noqa: E501

        Get a user permission set. Returns a list of the user’s permissions granted by the associated user's roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_user_permissions(user_id, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str): The ID of the user.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PermissionsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_user_permissions_endpoint.default_arguments(kwargs)
        kwargs["user_id"] = user_id
        return self._list_user_permissions_endpoint.call_with_http_info(**kwargs)

    def list_users(self, **kwargs):
        """List all users  # noqa: E501

        Get the list of all users in the organization. This list includes all users even if they are deactivated or unverified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_users(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page_size (int): Size for a given page.. [optional] if omitted the server will use the default value of 10
            page_number (int): Specific page number to return.. [optional] if omitted the server will use the default value of 0
            sort (str): User attribute to order results by. Sort order is ascending by default. Sort order is descending if the field is prefixed by a negative sign, for example `sort=-name`. Options: `name`, `modified_at`, `user_count`.. [optional] if omitted the server will use the default value of "name"
            sort_dir (QuerySortOrder): Direction of sort. Options: `asc`, `desc`.. [optional]
            filter (str): Filter all users by the given string. Defaults to no filtering.. [optional]
            filter_status (str): Filter on status attribute. Comma separated list, with possible values `Active`, `Pending`, and `Disabled`. Defaults to no filtering.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UsersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._list_users_endpoint.default_arguments(kwargs)
        return self._list_users_endpoint.call_with_http_info(**kwargs)

    def send_invitations(self, body, **kwargs):
        """Send invitation emails  # noqa: E501

        Sends emails to one or more users inviting them to join the organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_invitations(body, async_req=True)
        >>> result = thread.get()

        Args:
            body (UserInvitationsRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserInvitationsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._send_invitations_endpoint.default_arguments(kwargs)
        kwargs["body"] = body
        return self._send_invitations_endpoint.call_with_http_info(**kwargs)

    def update_user(self, user_id, body, **kwargs):
        """Update a user  # noqa: E501

        Edit a user. Can only be used with an application key belonging to an administrator user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user(user_id, body, async_req=True)
        >>> result = thread.get()

        Args:
            user_id (str): The ID of the user.
            body (UserUpdateRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (float/tuple): timeout setting for this request. If one
                number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            UserResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs = self._update_user_endpoint.default_arguments(kwargs)
        kwargs["user_id"] = user_id
        kwargs["body"] = body
        return self._update_user_endpoint.call_with_http_info(**kwargs)
