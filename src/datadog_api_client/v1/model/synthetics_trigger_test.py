# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_ci_batch_metadata import SyntheticsCIBatchMetadata

    globals()["SyntheticsCIBatchMetadata"] = SyntheticsCIBatchMetadata


class SyntheticsTriggerTest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "metadata": (SyntheticsCIBatchMetadata,),
            "public_id": (str,),
        }

    attribute_map = {
        "public_id": "public_id",
        "metadata": "metadata",
    }

    read_only_vars = {}

    def __init__(self, public_id, *args, **kwargs):
        """SyntheticsTriggerTest - a model defined in OpenAPI

        Args:
            public_id (str): The public ID of the Synthetics test to trigger.

        Keyword Args:
            metadata (SyntheticsCIBatchMetadata): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.public_id = public_id

    @classmethod
    def _from_openapi_data(cls, public_id, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTriggerTest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.public_id = public_id
        return self