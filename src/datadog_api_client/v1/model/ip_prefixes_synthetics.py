# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IPPrefixesSynthetics(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "prefixes_ipv4": ([str],),
            "prefixes_ipv4_by_location": ({str: ([str],)},),
            "prefixes_ipv6": ([str],),
            "prefixes_ipv6_by_location": ({str: ([str],)},),
        }

    attribute_map = {
        "prefixes_ipv4": "prefixes_ipv4",
        "prefixes_ipv4_by_location": "prefixes_ipv4_by_location",
        "prefixes_ipv6": "prefixes_ipv6",
        "prefixes_ipv6_by_location": "prefixes_ipv6_by_location",
    }

    def __init__(self_, *args, **kwargs):
        """
        Available prefix information for the Synthetics endpoints.

        :param prefixes_ipv4: List of IPv4 prefixes.
        :type prefixes_ipv4: [str], optional

        :param prefixes_ipv4_by_location: List of IPv4 prefixes by location.
        :type prefixes_ipv4_by_location: {str: ([str],)}, optional

        :param prefixes_ipv6: List of IPv6 prefixes.
        :type prefixes_ipv6: [str], optional

        :param prefixes_ipv6_by_location: List of IPv6 prefixes by location.
        :type prefixes_ipv6_by_location: {str: ([str],)}, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
