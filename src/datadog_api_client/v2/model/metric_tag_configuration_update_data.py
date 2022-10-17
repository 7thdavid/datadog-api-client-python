# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations
from datadog_api_client.v2.model.metric_tag_configuration_update_attributes import (
    MetricTagConfigurationUpdateAttributes,
)
from datadog_api_client.v2.model.metric_custom_aggregations import MetricCustomAggregations

if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType


@dataclass
class MetricTagConfigurationUpdateDataJSON:
    id: str
    aggregations: Union[MetricCustomAggregations, UnsetType] = unset
    include_percentiles: Union[bool, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset


class MetricTagConfigurationUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

        return {
            "attributes": (MetricTagConfigurationUpdateAttributes,),
            "id": (str,),
            "type": (MetricTagConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = MetricTagConfigurationUpdateDataJSON

    def __init__(
        self_,
        id: str,
        type: MetricTagConfigurationType,
        attributes: Union[MetricTagConfigurationUpdateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single tag configuration to be edited.

        :param attributes: Object containing the definition of a metric tag configuration to be updated.
        :type attributes: MetricTagConfigurationUpdateAttributes, optional

        :param id: The metric name for this resource.
        :type id: str

        :param type: The metric tag configuration resource type.
        :type type: MetricTagConfigurationType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
