# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.connectivity_constraint import ConnectivityConstraint  # noqa: F401,E501
from tapi_server.models.connectivity_service_end_point import ConnectivityServiceEndPoint  # noqa: F401,E501
from tapi_server.models.resilience_constraint import ResilienceConstraint  # noqa: F401,E501
from tapi_server.models.topology_constraint import TopologyConstraint  # noqa: F401,E501
from tapi_server import util


class UpdateConnectivityServiceRPCInputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, service_id_or_name: str=None, end_point: ConnectivityServiceEndPoint=None, conn_constraint: ConnectivityConstraint=None, topo_constraint: TopologyConstraint=None, resilience_constraint: List[ResilienceConstraint]=None, state: str=None):  # noqa: E501
        """UpdateConnectivityServiceRPCInputSchema - a model defined in Swagger

        :param service_id_or_name: The service_id_or_name of this UpdateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type service_id_or_name: str
        :param end_point: The end_point of this UpdateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type end_point: ConnectivityServiceEndPoint
        :param conn_constraint: The conn_constraint of this UpdateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type conn_constraint: ConnectivityConstraint
        :param topo_constraint: The topo_constraint of this UpdateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type topo_constraint: TopologyConstraint
        :param resilience_constraint: The resilience_constraint of this UpdateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type resilience_constraint: List[ResilienceConstraint]
        :param state: The state of this UpdateConnectivityServiceRPCInputSchema.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'service_id_or_name': str,
            'end_point': ConnectivityServiceEndPoint,
            'conn_constraint': ConnectivityConstraint,
            'topo_constraint': TopologyConstraint,
            'resilience_constraint': List[ResilienceConstraint],
            'state': str
        }

        self.attribute_map = {
            'service_id_or_name': 'service-id-or-name',
            'end_point': 'end-point',
            'conn_constraint': 'conn-constraint',
            'topo_constraint': 'topo-constraint',
            'resilience_constraint': 'resilience-constraint',
            'state': 'state'
        }

        self._service_id_or_name = service_id_or_name
        self._end_point = end_point
        self._conn_constraint = conn_constraint
        self._topo_constraint = topo_constraint
        self._resilience_constraint = resilience_constraint
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateConnectivityServiceRPCInputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The update-connectivity-serviceRPC_input_schema of this UpdateConnectivityServiceRPCInputSchema.  # noqa: E501
        :rtype: UpdateConnectivityServiceRPCInputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def service_id_or_name(self) -> str:
        """Gets the service_id_or_name of this UpdateConnectivityServiceRPCInputSchema.


        :return: The service_id_or_name of this UpdateConnectivityServiceRPCInputSchema.
        :rtype: str
        """
        return self._service_id_or_name

    @service_id_or_name.setter
    def service_id_or_name(self, service_id_or_name: str):
        """Sets the service_id_or_name of this UpdateConnectivityServiceRPCInputSchema.


        :param service_id_or_name: The service_id_or_name of this UpdateConnectivityServiceRPCInputSchema.
        :type service_id_or_name: str
        """

        self._service_id_or_name = service_id_or_name

    @property
    def end_point(self) -> ConnectivityServiceEndPoint:
        """Gets the end_point of this UpdateConnectivityServiceRPCInputSchema.


        :return: The end_point of this UpdateConnectivityServiceRPCInputSchema.
        :rtype: ConnectivityServiceEndPoint
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point: ConnectivityServiceEndPoint):
        """Sets the end_point of this UpdateConnectivityServiceRPCInputSchema.


        :param end_point: The end_point of this UpdateConnectivityServiceRPCInputSchema.
        :type end_point: ConnectivityServiceEndPoint
        """

        self._end_point = end_point

    @property
    def conn_constraint(self) -> ConnectivityConstraint:
        """Gets the conn_constraint of this UpdateConnectivityServiceRPCInputSchema.


        :return: The conn_constraint of this UpdateConnectivityServiceRPCInputSchema.
        :rtype: ConnectivityConstraint
        """
        return self._conn_constraint

    @conn_constraint.setter
    def conn_constraint(self, conn_constraint: ConnectivityConstraint):
        """Sets the conn_constraint of this UpdateConnectivityServiceRPCInputSchema.


        :param conn_constraint: The conn_constraint of this UpdateConnectivityServiceRPCInputSchema.
        :type conn_constraint: ConnectivityConstraint
        """

        self._conn_constraint = conn_constraint

    @property
    def topo_constraint(self) -> TopologyConstraint:
        """Gets the topo_constraint of this UpdateConnectivityServiceRPCInputSchema.


        :return: The topo_constraint of this UpdateConnectivityServiceRPCInputSchema.
        :rtype: TopologyConstraint
        """
        return self._topo_constraint

    @topo_constraint.setter
    def topo_constraint(self, topo_constraint: TopologyConstraint):
        """Sets the topo_constraint of this UpdateConnectivityServiceRPCInputSchema.


        :param topo_constraint: The topo_constraint of this UpdateConnectivityServiceRPCInputSchema.
        :type topo_constraint: TopologyConstraint
        """

        self._topo_constraint = topo_constraint

    @property
    def resilience_constraint(self) -> List[ResilienceConstraint]:
        """Gets the resilience_constraint of this UpdateConnectivityServiceRPCInputSchema.


        :return: The resilience_constraint of this UpdateConnectivityServiceRPCInputSchema.
        :rtype: List[ResilienceConstraint]
        """
        return self._resilience_constraint

    @resilience_constraint.setter
    def resilience_constraint(self, resilience_constraint: List[ResilienceConstraint]):
        """Sets the resilience_constraint of this UpdateConnectivityServiceRPCInputSchema.


        :param resilience_constraint: The resilience_constraint of this UpdateConnectivityServiceRPCInputSchema.
        :type resilience_constraint: List[ResilienceConstraint]
        """

        self._resilience_constraint = resilience_constraint

    @property
    def state(self) -> str:
        """Gets the state of this UpdateConnectivityServiceRPCInputSchema.


        :return: The state of this UpdateConnectivityServiceRPCInputSchema.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this UpdateConnectivityServiceRPCInputSchema.


        :param state: The state of this UpdateConnectivityServiceRPCInputSchema.
        :type state: str
        """

        self._state = state