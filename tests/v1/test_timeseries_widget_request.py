# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_query_definition import FormulaAndFunctionQueryDefinition
from datadog_api_client.v1.model.formula_and_function_response_format import FormulaAndFunctionResponseFormat
from datadog_api_client.v1.model.log_query_definition import LogQueryDefinition
from datadog_api_client.v1.model.process_query_definition import ProcessQueryDefinition
from datadog_api_client.v1.model.timeseries_widget_expression_alias import TimeseriesWidgetExpressionAlias
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_formula import WidgetFormula
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle

globals()["FormulaAndFunctionQueryDefinition"] = FormulaAndFunctionQueryDefinition
globals()["FormulaAndFunctionResponseFormat"] = FormulaAndFunctionResponseFormat
globals()["LogQueryDefinition"] = LogQueryDefinition
globals()["ProcessQueryDefinition"] = ProcessQueryDefinition
globals()["TimeseriesWidgetExpressionAlias"] = TimeseriesWidgetExpressionAlias
globals()["WidgetDisplayType"] = WidgetDisplayType
globals()["WidgetFormula"] = WidgetFormula
globals()["WidgetRequestStyle"] = WidgetRequestStyle
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest


class TestTimeseriesWidgetRequest(unittest.TestCase):
    """TimeseriesWidgetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeseriesWidgetRequest(self):
        """Test TimeseriesWidgetRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeseriesWidgetRequest()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
