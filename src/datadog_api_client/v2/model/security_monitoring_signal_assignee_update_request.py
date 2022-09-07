# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalAssigneeUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_assignee_update_data import (
            SecurityMonitoringSignalAssigneeUpdateData,
        )

        return {
            "data": (SecurityMonitoringSignalAssigneeUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        Request body for changing the assignee of a given security monitoring signal.

        :param data: Data containing the patch for changing the assignee of a signal.
        :type data: SecurityMonitoringSignalAssigneeUpdateData
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
