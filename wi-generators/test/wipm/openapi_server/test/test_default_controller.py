# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.inline_object import InlineObject  # noqa: E501
from openapi_server.models.inline_object1 import InlineObject1  # noqa: E501
from openapi_server.models.inline_object2 import InlineObject2  # noqa: E501
from openapi_server.models.inline_object3 import InlineObject3  # noqa: E501
from openapi_server.models.inline_object4 import InlineObject4  # noqa: E501
from openapi_server.models.inline_response201 import InlineResponse201  # noqa: E501
from openapi_server.models.inline_response2011 import InlineResponse2011  # noqa: E501
from openapi_server.models.inline_response2012 import InlineResponse2012  # noqa: E501
from openapi_server.models.inline_response2013 import InlineResponse2013  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_src_controllers_data_create(self):
        """Test case for src_controllers_data_create

        
        """
        inline_object1 = InlineObject1()
        response = self.client.open(
            '/api/data',
            method='POST',
            data=json.dumps(inline_object1),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_src_controllers_data_delete(self):
        """Test case for src_controllers_data_delete

        
        """
        inline_object2 = InlineObject2()
        response = self.client.open(
            '/api/data',
            method='DELETE',
            data=json.dumps(inline_object2),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_src_controllers_data_push(self):
        """Test case for src_controllers_data_push

        
        """
        inline_object = InlineObject()
        response = self.client.open(
            '/api/data',
            method='PUT',
            data=json.dumps(inline_object),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_src_controllers_predict(self):
        """Test case for src_controllers_predict

        
        """
        inline_object4 = InlineObject4()
        response = self.client.open(
            '/api/predict',
            method='POST',
            data=json.dumps(inline_object4),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_src_controllers_train(self):
        """Test case for src_controllers_train

        
        """
        inline_object3 = InlineObject3()
        response = self.client.open(
            '/api/train',
            method='POST',
            data=json.dumps(inline_object3),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
