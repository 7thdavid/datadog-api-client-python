# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricEstimateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_estimate import MetricEstimate

        return {
            "data": (MetricEstimate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response object that includes metric cardinality estimates.

        :param data: Object for a metric cardinality estimate.
        :type data: MetricEstimate, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)