import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import usage_metering_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = usage_metering_api.UsageMeteringApi(api_client)
    month = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to month: [YYYY-MM] for usage beginning at this hour. (Either month or day should be specified, but not both) (optional)
    day = dateutil_parser('1970-01-01T00:00:00.00Z')  # datetime | Datetime in ISO-8601 format, UTC, precise to day: [YYYY-MM-DD] for usage beginning at this hour. (Either month or day should be specified, but not both) (optional)
    names = [
        "names_example",
    ]  # [str] | Comma-separated list of metric names. (optional)
    limit = 500  # int | Maximum number of results to return (between 1 and 5000) - defaults to 500 results if limit not specified. (optional) if omitted the server will use the default value of 500
    next_record_id = "next_record_id_example"  # str | List following results with a next_record_id provided in the previous query. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all custom metrics by hourly average
        api_response = api_instance.get_usage_top_avg_metrics(month=month, day=day, names=names, limit=limit, next_record_id=next_record_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsageMeteringApi->get_usage_top_avg_metrics: %s\n" % e)