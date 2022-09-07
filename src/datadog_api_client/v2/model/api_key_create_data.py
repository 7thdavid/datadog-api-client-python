# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class APIKeyCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.api_key_create_attributes import APIKeyCreateAttributes
        from datadog_api_client.v2.model.api_keys_type import APIKeysType

        return {
            "attributes": (APIKeyCreateAttributes,),
            "type": (APIKeysType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes, type, *args, **kwargs):
        """
        Object used to create an API key.

        :param attributes: Attributes used to create an API Key.
        :type attributes: APIKeyCreateAttributes

        :param type: API Keys resource type.
        :type type: APIKeysType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.attributes = attributes
        self_.type = type
