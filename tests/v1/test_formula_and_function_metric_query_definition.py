# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.formula_and_function_metric_aggregation import FormulaAndFunctionMetricAggregation
from datadog_api_client.v1.model.formula_and_function_metric_data_source import FormulaAndFunctionMetricDataSource

globals()["FormulaAndFunctionMetricAggregation"] = FormulaAndFunctionMetricAggregation
globals()["FormulaAndFunctionMetricDataSource"] = FormulaAndFunctionMetricDataSource
from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
    FormulaAndFunctionMetricQueryDefinition,
)


class TestFormulaAndFunctionMetricQueryDefinition(unittest.TestCase):
    """FormulaAndFunctionMetricQueryDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFormulaAndFunctionMetricQueryDefinition(self):
        """Test FormulaAndFunctionMetricQueryDefinition"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FormulaAndFunctionMetricQueryDefinition()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()