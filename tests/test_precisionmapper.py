#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `precisionmapper` package."""

# To be tested with : python3 -m pytest -vs tests/test_precisionmapper.py

import pytest
import os
from precisionmapper import Survey

# Get useful environment variables
# VAR = os.environ.get('VAR', None)


def test_class_Survey():
    survey = Survey(
        id="123abc", name="My survey", drone_platform="DJI",
        sensor="RGB", location="Toulouse, France",
        date="2018-08-03T17:00:00.001Z", image_nb=3, size_in_MB=150,
        thumbnail="https://url_to_thumbnail.com", altitude_in_m=90,
        resolution_in_cm=2.5, area_in_ha=1.8)
    assert survey.id == "123abc"
    assert str(survey) == "[My survey] (Toulouse, France) : 3 images"


def test_class_MyClass_errors():
    with pytest.raises(TypeError):
        # Bad type for image number
        Survey(
            id="123abc", name="My survey", drone_platform="DJI",
            sensor="RGB", location="Toulouse, France",
            date="2018-08-03T17:00:00.001Z", image_nb="ABC", size_in_MB=150,
            thumbnail="https://url_to_thumbnail.com", altitude_in_m=90,
            resolution_in_cm=2.5, area_in_ha=1.8)

    with pytest.raises(TypeError):
        # Bad type for date
        Survey(
            id="123abc", name="My survey", drone_platform="DJI",
            sensor="RGB", location="Toulouse, France",
            date="not a date", image_nb=3, size_in_MB=150,
            thumbnail="https://url_to_thumbnail.com", altitude_in_m=90,
            resolution_in_cm=2.5, area_in_ha=1.8)
