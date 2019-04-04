import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.huber_parameter import HuberParameter  # noqa: E501
from openapi_server.models.inline_response2014 import InlineResponse2014  # noqa: E501
from openapi_server import util


def src_controllers_huber_create(huber_parameter=None):  # noqa: E501
    """src_controllers_huber_create

    Create Huber model # noqa: E501

    :param huber_parameter: 
    :type huber_parameter: dict | bytes

    :rtype: InlineResponse2014
    """
    if connexion.request.is_json:
        huber_parameter = HuberParameter.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
