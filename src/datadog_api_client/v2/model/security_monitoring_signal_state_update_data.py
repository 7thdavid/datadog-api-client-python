# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalStateUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_state_update_attributes import (
            SecurityMonitoringSignalStateUpdateAttributes,
        )

        return {
            "attributes": (SecurityMonitoringSignalStateUpdateAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(self_, attributes, *args, **kwargs):
        """
        Data containing the patch for changing the state of a signal.

        :param attributes: Attributes describing the change of state of a security signal.
        :type attributes: SecurityMonitoringSignalStateUpdateAttributes
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.attributes = attributes
