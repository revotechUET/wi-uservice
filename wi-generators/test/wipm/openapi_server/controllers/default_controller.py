import connexion
import six

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
from openapi_server import util


def src_controllers_data_create(inline_object1=None):  # noqa: E501
    """src_controllers_data_create

    Create bucket data # noqa: E501

    :param inline_object1: 
    :type inline_object1: dict | bytes

    :rtype: InlineResponse2011
    """
    if connexion.request.is_json:
        inline_object1 = InlineObject1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def src_controllers_data_delete(inline_object2=None):  # noqa: E501
    """src_controllers_data_delete

    Delete bucket data # noqa: E501

    :param inline_object2: 
    :type inline_object2: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        inline_object2 = InlineObject2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def src_controllers_data_push(inline_object=None):  # noqa: E501
    """src_controllers_data_push

    Push data into bucket # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def src_controllers_predict(inline_object4=None):  # noqa: E501
    """src_controllers_predict

    Predict model # noqa: E501

    :param inline_object4: 
    :type inline_object4: dict | bytes

    :rtype: InlineResponse2013
    """
    if connexion.request.is_json:
        inline_object4 = InlineObject4.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def src_controllers_train(inline_object3=None):  # noqa: E501
    """src_controllers_train

    Training model # noqa: E501

    :param inline_object3: 
    :type inline_object3: dict | bytes

    :rtype: InlineResponse2012
    """
    if connexion.request.is_json:
        inline_object3 = InlineObject3.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
