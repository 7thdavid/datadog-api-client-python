# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.api_client import ApiClient, Endpoint as _Endpoint
from datadog_api_client.model_utils import (
    datetime,
)
from datadog_api_client.v2.model.rum_events_response import RUMEventsResponse
from datadog_api_client.v2.model.rum_sort import RUMSort
from datadog_api_client.v2.model.rum_search_events_request import RUMSearchEventsRequest


class RUMApi:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        self._list_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/events",
                "operation_id": "list_rum_events",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "filter_query": {
                    "openapi_types": (str,),
                    "attribute": "filter[query]",
                    "location": "query",
                },
                "filter_from": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[from]",
                    "location": "query",
                },
                "filter_to": {
                    "openapi_types": (datetime,),
                    "attribute": "filter[to]",
                    "location": "query",
                },
                "sort": {
                    "openapi_types": (RUMSort,),
                    "attribute": "sort",
                    "location": "query",
                },
                "page_cursor": {
                    "openapi_types": (str,),
                    "attribute": "page[cursor]",
                    "location": "query",
                },
                "page_limit": {
                    "validation": {
                        "inclusive_maximum": 1000,
                    },
                    "openapi_types": (int,),
                    "attribute": "page[limit]",
                    "location": "query",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

        self._search_rum_events_endpoint = _Endpoint(
            settings={
                "response_type": (RUMEventsResponse,),
                "auth": ["apiKeyAuth", "appKeyAuth", "AuthZ"],
                "endpoint_path": "/api/v2/rum/events/search",
                "operation_id": "search_rum_events",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "body": {
                    "openapi_types": (RUMSearchEventsRequest,),
                    "location": "body",
                },
            },
            headers_map={"accept": ["application/json"], "content_type": ["application/json"]},
            api_client=api_client,
        )

    def list_rum_events(self, **kwargs):
        """Get a list of RUM events.

        List endpoint returns events that match a RUM search query.
        [Results are paginated][1].

        Use this endpoint to see your latest RUM events.

        [1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.list_rum_events(async_req=True)
        >>> result = thread.get()

        :param filter_query: Search query following RUM syntax.
        :type filter_query: str, optional
        :param filter_from: Minimum timestamp for requested events.
        :type filter_from: datetime, optional
        :param filter_to: Maximum timestamp for requested events.
        :type filter_to: datetime, optional
        :param sort: Order of events in results.
        :type sort: RUMSort, optional
        :param page_cursor: List following results with a cursor provided in the previous query.
        :type page_cursor: str, optional
        :param page_limit: Maximum number of events in the response.
        :type page_limit: int, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: RUMEventsResponse
        """
        kwargs = self._list_rum_events_endpoint.default_arguments(kwargs)
        return self._list_rum_events_endpoint.call_with_http_info(**kwargs)

    def search_rum_events(self, **kwargs):
        """Search RUM events.

        List endpoint returns RUM events that match a RUM search query.
        [Results are paginated][1].

        Use this endpoint to build complex RUM events filtering and search.

        [1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.

        >>> thread = api.search_rum_events(async_req=True)
        >>> result = thread.get()


        :type body: RUMSearchEventsRequest, optional
        :param _return_http_data_only: Response data without head status
            code and headers. Default is True.
        :type _return_http_data_only: bool
        :param _preload_content: If False, the urllib3.HTTPResponse object
            will be returned without reading/decoding response data.
            Default is True.
        :type _preload_content: bool
        :param _request_timeout: Timeout setting for this request. If one
            number provided, it will be total request timeout. It can also be a
            pair (tuple) of (connection, read) timeouts.  Default is None.
        :type _request_timeout: float/tuple
        :param _check_input_type: Specifies if type checking should be done one
            the data sent to the server. Default is True.
        :type _check_input_type: bool
        :param _check_return_type: Specifies if type checking should be done
            one the data received from the server. Default is True.
        :type _check_return_type: bool
        :param _host_index: Specifies the index of the server that we want to
            use. Default is read from the configuration.
        :type _host_index: int/None
        :param async_req: Execute request asynchronously.
        :type async_req: bool

        :return: If the method is called asynchronously, returns the request thread.
        :rtype: RUMEventsResponse
        """
        kwargs = self._search_rum_events_endpoint.default_arguments(kwargs)
        return self._search_rum_events_endpoint.call_with_http_info(**kwargs)