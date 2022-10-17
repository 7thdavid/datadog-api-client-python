# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.saml_assertion_attribute_attributes import SAMLAssertionAttributeAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.saml_assertion_attributes_type import SAMLAssertionAttributesType


@dataclass
class SAMLAssertionAttributeJSON:
    id: str
    attribute_key: Union[str, UnsetType] = unset
    attribute_value: Union[str, UnsetType] = unset


class SAMLAssertionAttribute(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.saml_assertion_attributes_type import SAMLAssertionAttributesType

        return {
            "attributes": (SAMLAssertionAttributeAttributes,),
            "id": (str,),
            "type": (SAMLAssertionAttributesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = SAMLAssertionAttributeJSON

    def __init__(
        self_,
        id: str,
        type: SAMLAssertionAttributesType,
        attributes: Union[SAMLAssertionAttributeAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        SAML assertion attribute.

        :param attributes: Key/Value pair of attributes used in SAML assertion attributes.
        :type attributes: SAMLAssertionAttributeAttributes, optional

        :param id: The ID of the SAML assertion attribute.
        :type id: str

        :param type: SAML assertion attributes resource type.
        :type type: SAMLAssertionAttributesType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
