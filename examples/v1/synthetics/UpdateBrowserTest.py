"""
Edit a browser test returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.http_method import HTTPMethod
from datadog_api_client.v1.model.synthetics_basic_auth_web import SyntheticsBasicAuthWeb
from datadog_api_client.v1.model.synthetics_basic_auth_web_type import SyntheticsBasicAuthWebType
from datadog_api_client.v1.model.synthetics_browser_test import SyntheticsBrowserTest
from datadog_api_client.v1.model.synthetics_browser_test_config import SyntheticsBrowserTestConfig
from datadog_api_client.v1.model.synthetics_browser_test_type import SyntheticsBrowserTestType
from datadog_api_client.v1.model.synthetics_browser_variable import SyntheticsBrowserVariable
from datadog_api_client.v1.model.synthetics_browser_variable_type import SyntheticsBrowserVariableType
from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType
from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
from datadog_api_client.v1.model.synthetics_step import SyntheticsStep
from datadog_api_client.v1.model.synthetics_step_type import SyntheticsStepType
from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
from datadog_api_client.v1.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
from datadog_api_client.v1.model.synthetics_test_request_certificate import SyntheticsTestRequestCertificate
from datadog_api_client.v1.model.synthetics_test_request_certificate_item import SyntheticsTestRequestCertificateItem
from datadog_api_client.v1.model.synthetics_test_request_proxy import SyntheticsTestRequestProxy

body = SyntheticsBrowserTest(
    config=SyntheticsBrowserTestConfig(
        assertions=[],
        config_variables=[SyntheticsConfigVariable(name="VARIABLE_NAME", type=SyntheticsConfigVariableType("text"))],
        request=SyntheticsTestRequest(
            basic_auth=SyntheticsBasicAuthWeb(
                password="PaSSw0RD!", type=SyntheticsBasicAuthWebType("web"), username="my_username"
            ),
            certificate=SyntheticsTestRequestCertificate(
                cert=SyntheticsTestRequestCertificateItem(), key=SyntheticsTestRequestCertificateItem()
            ),
            method=HTTPMethod("GET"),
            proxy=SyntheticsTestRequestProxy(url="https://example.com"),
            url="https://example.com",
        ),
        variables=[SyntheticsBrowserVariable(name="VARIABLE_NAME", type=SyntheticsBrowserVariableType("text"))],
    ),
    locations=["aws:eu-west-3"],
    message="",
    name="Example test name",
    options=SyntheticsTestOptions(
        device_ids=[SyntheticsDeviceID("laptop_large")],
        monitor_options=SyntheticsTestOptionsMonitorOptions(),
        retry=SyntheticsTestOptionsRetry(),
    ),
    status=SyntheticsTestPauseStatus("live"),
    steps=[SyntheticsStep(type=SyntheticsStepType("assertElementContent"))],
    tags=["env:prod"],
    type=SyntheticsBrowserTestType("browser"),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.update_browser_test(public_id="public_id", body=body)

    print(response)