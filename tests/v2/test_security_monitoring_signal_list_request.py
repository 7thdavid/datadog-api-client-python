# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.security_monitoring_signal_list_request_filter import (
    SecurityMonitoringSignalListRequestFilter,
)
from datadog_api_client.v2.model.security_monitoring_signal_list_request_page import (
    SecurityMonitoringSignalListRequestPage,
)
from datadog_api_client.v2.model.security_monitoring_signals_sort import SecurityMonitoringSignalsSort

globals()["SecurityMonitoringSignalListRequestFilter"] = SecurityMonitoringSignalListRequestFilter
globals()["SecurityMonitoringSignalListRequestPage"] = SecurityMonitoringSignalListRequestPage
globals()["SecurityMonitoringSignalsSort"] = SecurityMonitoringSignalsSort
from datadog_api_client.v2.model.security_monitoring_signal_list_request import SecurityMonitoringSignalListRequest


class TestSecurityMonitoringSignalListRequest(unittest.TestCase):
    """SecurityMonitoringSignalListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityMonitoringSignalListRequest(self):
        """Test SecurityMonitoringSignalListRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityMonitoringSignalListRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
