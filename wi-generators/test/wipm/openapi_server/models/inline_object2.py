# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bucket_id=None):  # noqa: E501
        """InlineObject2 - a model defined in OpenAPI

        :param bucket_id: The bucket_id of this InlineObject2.  # noqa: E501
        :type bucket_id: str
        """
        self.openapi_types = {
            'bucket_id': 'str'
        }

        self.attribute_map = {
            'bucket_id': 'bucket_id'
        }

        self._bucket_id = bucket_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object_2 of this InlineObject2.  # noqa: E501
        :rtype: InlineObject2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bucket_id(self):
        """Gets the bucket_id of this InlineObject2.


        :return: The bucket_id of this InlineObject2.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this InlineObject2.


        :param bucket_id: The bucket_id of this InlineObject2.
        :type bucket_id: str
        """
        if bucket_id is None:
            raise ValueError("Invalid value for `bucket_id`, must not be `None`")  # noqa: E501

        self._bucket_id = bucket_id
