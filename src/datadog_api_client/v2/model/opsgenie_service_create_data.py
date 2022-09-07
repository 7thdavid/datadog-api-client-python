# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OpsgenieServiceCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_service_create_attributes import OpsgenieServiceCreateAttributes
        from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType

        return {
            "attributes": (OpsgenieServiceCreateAttributes,),
            "type": (OpsgenieServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes, type, *args, **kwargs):
        """
        Opsgenie service data for a create request.

        :param attributes: The Opsgenie service attributes for a create request.
        :type attributes: OpsgenieServiceCreateAttributes

        :param type: Opsgenie service resource type.
        :type type: OpsgenieServiceType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.attributes = attributes
        self_.type = type
