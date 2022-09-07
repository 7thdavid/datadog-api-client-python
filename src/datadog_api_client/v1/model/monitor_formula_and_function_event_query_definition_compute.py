# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorFormulaAndFunctionEventQueryDefinitionCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_event_aggregation import (
            MonitorFormulaAndFunctionEventAggregation,
        )

        return {
            "aggregation": (MonitorFormulaAndFunctionEventAggregation,),
            "interval": (int,),
            "metric": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
    }

    def __init__(self_, aggregation, *args, **kwargs):
        """
        Compute options.

        :param aggregation: Aggregation methods for event platform queries.
        :type aggregation: MonitorFormulaAndFunctionEventAggregation

        :param interval: A time interval in milliseconds.
        :type interval: int, optional

        :param metric: Measurable attribute to compute.
        :type metric: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.aggregation = aggregation
