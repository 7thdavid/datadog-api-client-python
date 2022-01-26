# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.sunburst_widget_definition_type import SunburstWidgetDefinitionType
    from datadog_api_client.v1.model.sunburst_widget_legend import SunburstWidgetLegend
    from datadog_api_client.v1.model.sunburst_widget_request import SunburstWidgetRequest
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["SunburstWidgetDefinitionType"] = SunburstWidgetDefinitionType
    globals()["SunburstWidgetLegend"] = SunburstWidgetLegend
    globals()["SunburstWidgetRequest"] = SunburstWidgetRequest
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class SunburstWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {
        "requests": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "custom_links": ([WidgetCustomLink],),
            "hide_total": (bool,),
            "legend": (SunburstWidgetLegend,),
            "requests": ([SunburstWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (SunburstWidgetDefinitionType,),
        }

    attribute_map = {
        "requests": "requests",
        "type": "type",
        "custom_links": "custom_links",
        "hide_total": "hide_total",
        "legend": "legend",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """SunburstWidgetDefinition - a model defined in OpenAPI

        Args:
            requests ([SunburstWidgetRequest]): List of sunburst widget requests.
            type (SunburstWidgetDefinitionType):

        Keyword Args:
            custom_links ([WidgetCustomLink]): [optional] List of custom links.
            hide_total (bool): [optional] Show the total value in this widget.
            legend (SunburstWidgetLegend): [optional]
            time (WidgetTime): [optional]
            title (str): [optional] Title of your widget.
            title_align (WidgetTextAlign): [optional]
            title_size (str): [optional] Size of the title.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SunburstWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self