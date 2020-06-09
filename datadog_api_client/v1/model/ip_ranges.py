# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)
try:
    from datadog_api_client.v1.model import ip_prefixes_agents
except ImportError:
    ip_prefixes_agents = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_agents']
try:
    from datadog_api_client.v1.model import ip_prefixes_api
except ImportError:
    ip_prefixes_api = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_api']
try:
    from datadog_api_client.v1.model import ip_prefixes_apm
except ImportError:
    ip_prefixes_apm = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_apm']
try:
    from datadog_api_client.v1.model import ip_prefixes_logs
except ImportError:
    ip_prefixes_logs = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_logs']
try:
    from datadog_api_client.v1.model import ip_prefixes_process
except ImportError:
    ip_prefixes_process = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_process']
try:
    from datadog_api_client.v1.model import ip_prefixes_synthetics
except ImportError:
    ip_prefixes_synthetics = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_synthetics']
try:
    from datadog_api_client.v1.model import ip_prefixes_webhooks
except ImportError:
    ip_prefixes_webhooks = sys.modules[
        'datadog_api_client.v1.model.ip_prefixes_webhooks']


class IPRanges(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'agents': (ip_prefixes_agents.IPPrefixesAgents,),  # noqa: E501
            'api': (ip_prefixes_api.IPPrefixesAPI,),  # noqa: E501
            'apm': (ip_prefixes_apm.IPPrefixesAPM,),  # noqa: E501
            'logs': (ip_prefixes_logs.IPPrefixesLogs,),  # noqa: E501
            'modified': (str,),  # noqa: E501
            'process': (ip_prefixes_process.IPPrefixesProcess,),  # noqa: E501
            'synthetics': (ip_prefixes_synthetics.IPPrefixesSynthetics,),  # noqa: E501
            'version': (int,),  # noqa: E501
            'webhooks': (ip_prefixes_webhooks.IPPrefixesWebhooks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'agents': 'agents',  # noqa: E501
        'api': 'api',  # noqa: E501
        'apm': 'apm',  # noqa: E501
        'logs': 'logs',  # noqa: E501
        'modified': 'modified',  # noqa: E501
        'process': 'process',  # noqa: E501
        'synthetics': 'synthetics',  # noqa: E501
        'version': 'version',  # noqa: E501
        'webhooks': 'webhooks',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ip_ranges.IPRanges - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            agents (ip_prefixes_agents.IPPrefixesAgents): [optional]  # noqa: E501
            api (ip_prefixes_api.IPPrefixesAPI): [optional]  # noqa: E501
            apm (ip_prefixes_apm.IPPrefixesAPM): [optional]  # noqa: E501
            logs (ip_prefixes_logs.IPPrefixesLogs): [optional]  # noqa: E501
            modified (str): Date when last updated, in the form &#x60;YYYY-MM-DD-hh-mm-ss&#x60;.. [optional]  # noqa: E501
            process (ip_prefixes_process.IPPrefixesProcess): [optional]  # noqa: E501
            synthetics (ip_prefixes_synthetics.IPPrefixesSynthetics): [optional]  # noqa: E501
            version (int): Version of the IP list.. [optional]  # noqa: E501
            webhooks (ip_prefixes_webhooks.IPPrefixesWebhooks): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
