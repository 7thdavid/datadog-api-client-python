# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_aggregate_response_status import LogsAggregateResponseStatus
from datadog_api_client.v2.model.logs_response_metadata_page import LogsResponseMetadataPage
from datadog_api_client.v2.model.logs_warning import LogsWarning

globals()["LogsAggregateResponseStatus"] = LogsAggregateResponseStatus
globals()["LogsResponseMetadataPage"] = LogsResponseMetadataPage
globals()["LogsWarning"] = LogsWarning
from datadog_api_client.v2.model.logs_response_metadata import LogsResponseMetadata


class TestLogsResponseMetadata(unittest.TestCase):
    """LogsResponseMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsResponseMetadata(self):
        """Test LogsResponseMetadata"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsResponseMetadata()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
