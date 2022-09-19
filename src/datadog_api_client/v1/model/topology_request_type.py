# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TopologyRequestType(ModelSimple):
    """
    Widget request type.

    :param value: If omitted defaults to "topology". Must be one of ["topology"].
    :type value: str
    """

    allowed_values = {
        "topology",
    }
    TOPOLOGY: ClassVar["TopologyRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TopologyRequestType.TOPOLOGY = TopologyRequestType("topology")