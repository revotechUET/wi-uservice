# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bucket_id=None, data=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI

        :param bucket_id: The bucket_id of this InlineObject.  # noqa: E501
        :type bucket_id: str
        :param data: The data of this InlineObject.  # noqa: E501
        :type data: Features
        """
        self.openapi_types = {
            'bucket_id': 'str',
            'data': 'Features'
        }

        self.attribute_map = {
            'bucket_id': 'bucket_id',
            'data': 'data'
        }

        self._bucket_id = bucket_id
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object of this InlineObject.  # noqa: E501
        :rtype: InlineObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bucket_id(self):
        """Gets the bucket_id of this InlineObject.


        :return: The bucket_id of this InlineObject.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this InlineObject.


        :param bucket_id: The bucket_id of this InlineObject.
        :type bucket_id: str
        """
        if bucket_id is None:
            raise ValueError("Invalid value for `bucket_id`, must not be `None`")  # noqa: E501

        self._bucket_id = bucket_id

    @property
    def data(self):
        """Gets the data of this InlineObject.


        :return: The data of this InlineObject.
        :rtype: Features
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineObject.


        :param data: The data of this InlineObject.
        :type data: Features
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data
