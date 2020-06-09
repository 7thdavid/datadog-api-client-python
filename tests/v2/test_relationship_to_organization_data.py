# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import sys
import unittest

import datadog_api_client.v2
try:
    from datadog_api_client.v2.model import organizations_type
except ImportError:
    organizations_type = sys.modules[
        'datadog_api_client.v2.model.organizations_type']
from datadog_api_client.v2.model.relationship_to_organization_data import RelationshipToOrganizationData


class TestRelationshipToOrganizationData(unittest.TestCase):
    """RelationshipToOrganizationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRelationshipToOrganizationData(self):
        """Test RelationshipToOrganizationData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RelationshipToOrganizationData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
