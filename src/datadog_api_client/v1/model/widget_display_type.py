# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WidgetDisplayType(ModelSimple):
    """
    Type of display to use for the request.

    :param value: Must be one of ["area", "bars", "line"].
    :type value: str
    """

    allowed_values = {
        "area",
        "bars",
        "line",
    }
    AREA: ClassVar["WidgetDisplayType"]
    BARS: ClassVar["WidgetDisplayType"]
    LINE: ClassVar["WidgetDisplayType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetDisplayType.AREA = WidgetDisplayType("area")
WidgetDisplayType.BARS = WidgetDisplayType("bars")
WidgetDisplayType.LINE = WidgetDisplayType("line")
