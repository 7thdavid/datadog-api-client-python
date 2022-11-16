# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_report_create import DashboardReportCreate


class DashboardReportCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_report_create import DashboardReportCreate

        return {
            "data": (DashboardReportCreate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DashboardReportCreate, **kwargs):
        """
        Request body when creating a new dashboard report.

        :param data: Schema for request body to create a dashboard report.
        :type data: DashboardReportCreate
        """
        super().__init__(kwargs)

        self_.data = data
