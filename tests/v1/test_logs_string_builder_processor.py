# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.logs_string_builder_processor_type import LogsStringBuilderProcessorType

globals()["LogsStringBuilderProcessorType"] = LogsStringBuilderProcessorType
from datadog_api_client.v1.model.logs_string_builder_processor import LogsStringBuilderProcessor


class TestLogsStringBuilderProcessor(unittest.TestCase):
    """LogsStringBuilderProcessor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsStringBuilderProcessor(self):
        """Test LogsStringBuilderProcessor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsStringBuilderProcessor()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
