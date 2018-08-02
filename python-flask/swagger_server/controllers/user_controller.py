import connexion
import six

from swagger_server.models.survey import Survey  # noqa: E501
from swagger_server import util


def get_surveys():  # noqa: E501
    """list the surveys available

    List the surveys available # noqa: E501


    :rtype: List[Survey]
    """
    return 'do some magic!'
