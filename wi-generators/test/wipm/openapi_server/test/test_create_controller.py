# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.huber_parameter import HuberParameter  # noqa: E501
from openapi_server.models.inline_response2014 import InlineResponse2014  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCreateController(BaseTestCase):
    """CreateController integration test stubs"""

    def test_src_controllers_huber_create(self):
        """Test case for src_controllers_huber_create

        
        """
        huber_parameter = HuberParameter()
        response = self.client.open(
            '/api/huber_create',
            method='POST',
            data=json.dumps(huber_parameter),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
