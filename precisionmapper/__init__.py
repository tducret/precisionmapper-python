# -*- coding: utf-8 -*-

"""Top-level package for PrecisionMapper."""

import requests
from requests import ConnectionError
from datetime import datetime
from bs4 import BeautifulSoup

__author__ = """Thibault Ducret"""
__email__ = 'hello@tducret.com'
__version__ = '0.0.1'

_DEFAULT_BEAUTIFULSOUP_PARSER = "html.parser"
_SIGNIN_URL = 'https://www.precisionmapper.com/users/sign_in'

_AUTHENTICITY_TOKEN_SELECTOR = 'meta["name"="csrf-token"]'


class Client(object):
    """ Do the requests with the servers """
    def __init__(self):
        self.session = requests.session()
        self.headers = {
                        'authority': 'www.precisionmapper.com',
                        'origin': 'https://www.precisionmapper.com',
                        'user-Agent': 'Mozilla/5.0 (Macintosh; \
Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/67.0.3396.99 Safari/537.36',
                        'referer': 'https://www.precisionmapper.com\
/users/sign_in',
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


class PrecisionMapper(object):
    """ Class for the communications with precisionmapper.com """
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.client = Client()

    def __str__(self):
        return(repr(self))

    def __repr__(self):
        return("PrecisionMapper(login={})".format(self.login))

    def get_surveys(self):
        """ Function to get the surveys for the account """
        return

    def get_authenticity_token(self, url=_SIGNIN_URL):
        """ Returns an authenticity_token, mandatory for signing in """
        res = self.client._get(url=url, expected_status_code=200)
        soup = BeautifulSoup(res.text, _DEFAULT_BEAUTIFULSOUP_PARSER)
        selection = soup.select(_AUTHENTICITY_TOKEN_SELECTOR)
        try:
            authenticity_token = selection[0].get("content")
        except:
            raise ValueError(
                "authenticity_token not found in {} with {}\n{}".format(
                 _SIGNIN_URL, _AUTHENTICITY_TOKEN_SELECTOR, res.text))
        return authenticity_token

    def sign_in(self):
        authenticity_token = self.get_authenticity_token()
        post_data = {"utf8": "✓",
                     "authenticity_token": authenticity_token,
                     "return": "",
                     "login[username]": self.login,
                     "login[password]": self.password,
                     "commit": "Log In"}
        res = self.client._post(
            url=_SIGNIN_URL, post_data=post_data,
            expected_status_code=200)
        return(res.text)


def _css_select(soup, css_selector):
        """ Returns the content of the element pointed by the CSS selector,
        or an empty string if not found """
        selection = soup.select(css_selector)
        if len(selection) > 0:
            if hasattr(selection[0], 'text'):
                retour = selection[0].text.strip()
            else:
                retour = ""
        else:
            retour = ""
        return retour
