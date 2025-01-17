# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_search_response_data import IncidentSearchResponseData
    from datadog_api_client.v2.model.incident_response_included_item import IncidentResponseIncludedItem
    from datadog_api_client.v2.model.user import User
    from datadog_api_client.v2.model.incident_attachment_data import IncidentAttachmentData


class IncidentSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_search_response_data import IncidentSearchResponseData
        from datadog_api_client.v2.model.incident_response_included_item import IncidentResponseIncludedItem

        return {
            "data": (IncidentSearchResponseData,),
            "included": ([IncidentResponseIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }
    read_only_vars = {
        "included",
    }

    def __init__(
        self_,
        data: IncidentSearchResponseData,
        included: Union[List[Union[IncidentResponseIncludedItem, User, IncidentAttachmentData]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response with incidents and facets.

        :param data: Data returned by an incident search.
        :type data: IncidentSearchResponseData

        :param included: Included related resources that the user requested.
        :type included: [IncidentResponseIncludedItem], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
