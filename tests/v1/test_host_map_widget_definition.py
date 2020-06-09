# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v1
try:
    from datadog_api_client.v1.model import host_map_widget_definition_requests
except ImportError:
    host_map_widget_definition_requests = sys.modules[
        'datadog_api_client.v1.model.host_map_widget_definition_requests']
try:
    from datadog_api_client.v1.model import host_map_widget_definition_style
except ImportError:
    host_map_widget_definition_style = sys.modules[
        'datadog_api_client.v1.model.host_map_widget_definition_style']
try:
    from datadog_api_client.v1.model import host_map_widget_definition_type
except ImportError:
    host_map_widget_definition_type = sys.modules[
        'datadog_api_client.v1.model.host_map_widget_definition_type']
try:
    from datadog_api_client.v1.model import widget_node_type
except ImportError:
    widget_node_type = sys.modules[
        'datadog_api_client.v1.model.widget_node_type']
try:
    from datadog_api_client.v1.model import widget_text_align
except ImportError:
    widget_text_align = sys.modules[
        'datadog_api_client.v1.model.widget_text_align']
from datadog_api_client.v1.model.host_map_widget_definition import HostMapWidgetDefinition


class TestHostMapWidgetDefinition(unittest.TestCase):
    """HostMapWidgetDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHostMapWidgetDefinition(self):
        """Test HostMapWidgetDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HostMapWidgetDefinition()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
