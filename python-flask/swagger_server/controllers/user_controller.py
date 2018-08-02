import connexion
import six

from swagger_server.models.survey import Survey  # noqa: E501
from swagger_server import util

from precisionmapper import PrecisionMapper
import os

# Get useful environment variables
_LOGIN = os.environ.get('PRECISIONMAPPER_LOGIN', None)
_PASSWORD = os.environ.get('PRECISIONMAPPER_PASSWORD', None)


def list_surveys():  # noqa: E501
    """list the surveys available

    List the surveys available # noqa: E501


    :rtype: List[Survey]
    """
    pm = PrecisionMapper(login=_LOGIN, password=_PASSWORD)
    pm.sign_in()
    shared_surveys = pm.get_shared_surveys()

    for survey in shared_surveys:
        print(survey)
    return 'do some magic!'
