# -*- coding: utf-8 -*-

"""Top-level package for PrecisionMapper."""

import requests
from requests import ConnectionError
from datetime import datetime

__author__ = """Thibault Ducret"""
__email__ = 'hello@tducret.com'
__version__ = '0.0.1'


class Client(object):
    """ Do the requests with the servers """
    def __init__(self):
        self.session = requests.session()
        self.headers = {
                    'Host': 'myhost.com',
                    'User-Agent': 'User agent',
                    }

    def _get(self, url, expected_status_code=200):
        ret = self.session.get(url=url, headers=self.headers)
        if (ret.status_code != expected_status_code):
            raise ConnectionError(
                'Status code {status} for url {url}\n{content}'.format(
                    status=ret.status_code, url=url, content=ret.text))
        return ret

    def _post(self, url, post_data, expected_status_code=200):
        ret = self.session.post(url=url,
                                headers=self.headers,
                                data=post_data)
        if (ret.status_code != expected_status_code):
            raise ConnectionError(
                'Status code {status} for url {url}\n{content}'.format(
                    status=ret.status_code, url=url, content=ret.text))
        return ret


class Survey(object):
    """ Class for a drone survey (mission) """
    def __init__(
            self, id, name, drone_platform, sensor, location,
            date, image_nb, size_in_MB, thumbnail, altitude_in_m,
            resolution_in_cm, area_in_ha):

        if type(id) != str:
            raise TypeError("id must be a string, not a "+type(id))
        self.id = id
        if type(image_nb) != int:
            raise TypeError("image_nb must be an int, not a "+type(image_nb))
        self.image_nb = image_nb
        try:
            self.date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
        except:
            raise TypeError("date must respect the format \
                         YYYY-MM-DDTHH:MM:SS.sssZ,received : "+date)

        self.name = name
        self.drone_platform = drone_platform
        self.sensor = sensor
        self.location = location

        self.size_in_MB = size_in_MB
        self.thumbnail = thumbnail
        self.altitude_in_m = altitude_in_m
        self.resolution_in_cm = resolution_in_cm
        self.area_in_ha = area_in_ha

    def __str__(self):
        return('[{name}] ({location}) : {image_nb} images'.format(
            name=self.name,
            location=self.location,
            image_nb=self.image_nb))

    def __repr__(self):
        return("Survey(id={}, name={})".format(self.id, self.name))
