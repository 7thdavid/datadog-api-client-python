# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.synthetics_browser_test_result_short import SyntheticsBrowserTestResultShort

globals()["SyntheticsBrowserTestResultShort"] = SyntheticsBrowserTestResultShort
from datadog_api_client.v1.model.synthetics_get_browser_test_latest_results_response import (
    SyntheticsGetBrowserTestLatestResultsResponse,
)


class TestSyntheticsGetBrowserTestLatestResultsResponse(unittest.TestCase):
    """SyntheticsGetBrowserTestLatestResultsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSyntheticsGetBrowserTestLatestResultsResponse(self):
        """Test SyntheticsGetBrowserTestLatestResultsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SyntheticsGetBrowserTestLatestResultsResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
