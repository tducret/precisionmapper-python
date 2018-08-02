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
    surveys = pm.get_surveys()

    survey_list = []
    for survey in surveys:
        survey_obj = Survey(
            date=survey.date, image_nb=survey.image_nb,
            location=survey.location, name=survey.name,
            sensors=survey.sensor, size=survey.size, survey_id=survey.id)
        survey_list.append(survey_obj)
    return survey_list
