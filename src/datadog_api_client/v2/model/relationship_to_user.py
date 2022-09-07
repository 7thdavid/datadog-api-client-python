# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RelationshipToUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user_data import RelationshipToUserData

        return {
            "data": (RelationshipToUserData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        Relationship to user.

        :param data: Relationship to user object.
        :type data: RelationshipToUserData
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
