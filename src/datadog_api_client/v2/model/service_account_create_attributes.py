# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceAccountCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "name": (str,),
            "service_account": (bool,),
            "title": (str,),
        }

    attribute_map = {
        "email": "email",
        "name": "name",
        "service_account": "service_account",
        "title": "title",
    }

    def __init__(self_, email, service_account, *args, **kwargs):
        """
        Attributes of the created user.

        :param email: The email of the user.
        :type email: str

        :param name: The name of the user.
        :type name: str, optional

        :param service_account: Whether the user is a service account. Must be true.
        :type service_account: bool

        :param title: The title of the user.
        :type title: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.email = email
        self_.service_account = service_account
