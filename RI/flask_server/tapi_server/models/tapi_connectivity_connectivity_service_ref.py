# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiConnectivityConnectivityServiceRef(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, connectivity_service_uuid=None):  # noqa: E501
        """TapiConnectivityConnectivityServiceRef - a model defined in OpenAPI

        :param connectivity_service_uuid: The connectivity_service_uuid of this TapiConnectivityConnectivityServiceRef.  # noqa: E501
        :type connectivity_service_uuid: str
        """
        self.openapi_types = {
            'connectivity_service_uuid': str
        }

        self.attribute_map = {
            'connectivity_service_uuid': 'connectivity-service-uuid'
        }

        self._connectivity_service_uuid = connectivity_service_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityConnectivityServiceRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.ConnectivityServiceRef of this TapiConnectivityConnectivityServiceRef.  # noqa: E501
        :rtype: TapiConnectivityConnectivityServiceRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def connectivity_service_uuid(self):
        """Gets the connectivity_service_uuid of this TapiConnectivityConnectivityServiceRef.

        none  # noqa: E501

        :return: The connectivity_service_uuid of this TapiConnectivityConnectivityServiceRef.
        :rtype: str
        """
        return self._connectivity_service_uuid

    @connectivity_service_uuid.setter
    def connectivity_service_uuid(self, connectivity_service_uuid):
        """Sets the connectivity_service_uuid of this TapiConnectivityConnectivityServiceRef.

        none  # noqa: E501

        :param connectivity_service_uuid: The connectivity_service_uuid of this TapiConnectivityConnectivityServiceRef.
        :type connectivity_service_uuid: str
        """

        self._connectivity_service_uuid = connectivity_service_uuid
