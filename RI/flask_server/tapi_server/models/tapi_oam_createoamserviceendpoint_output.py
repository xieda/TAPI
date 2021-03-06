# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_oam_oam_service_end_point import TapiOamOamServiceEndPoint  # noqa: F401,E501
from tapi_server import util


class TapiOamCreateoamserviceendpointOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, end_point=None):  # noqa: E501
        """TapiOamCreateoamserviceendpointOutput - a model defined in OpenAPI

        :param end_point: The end_point of this TapiOamCreateoamserviceendpointOutput.  # noqa: E501
        :type end_point: TapiOamOamServiceEndPoint
        """
        self.openapi_types = {
            'end_point': TapiOamOamServiceEndPoint
        }

        self.attribute_map = {
            'end_point': 'end-point'
        }

        self._end_point = end_point

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamCreateoamserviceendpointOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.createoamserviceendpoint.Output of this TapiOamCreateoamserviceendpointOutput.  # noqa: E501
        :rtype: TapiOamCreateoamserviceendpointOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def end_point(self):
        """Gets the end_point of this TapiOamCreateoamserviceendpointOutput.


        :return: The end_point of this TapiOamCreateoamserviceendpointOutput.
        :rtype: TapiOamOamServiceEndPoint
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this TapiOamCreateoamserviceendpointOutput.


        :param end_point: The end_point of this TapiOamCreateoamserviceendpointOutput.
        :type end_point: TapiOamOamServiceEndPoint
        """

        self._end_point = end_point
