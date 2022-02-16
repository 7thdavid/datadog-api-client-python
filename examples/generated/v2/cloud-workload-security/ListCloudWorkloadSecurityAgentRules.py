import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import cloud_workload_security_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_workload_security_api.CloudWorkloadSecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all Cloud Workload Security Agent rules
        api_response = api_instance.list_cloud_workload_security_agent_rules()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudWorkloadSecurityApi->list_cloud_workload_security_agent_rules: %s\n" % e)