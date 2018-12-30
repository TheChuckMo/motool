# coding=utf-8
"""pytest fixtures for testing"""

import pytest

import os, json


@pytest.fixture(scope="module")
def vector_values():
    """
    load vectors and answers from file test_vector_values.json

    Returns: dict of vector values for testing

    """
    _values = {}
    _dir = os.path.dirname(os.path.abspath(__file__))
    _fire = os.path.join(_dir, 'test_vector_values.json')

    if os.path.isfile(_fire):
        with open(_fire, 'r') as fh:
            _values = json.load(fh)

    return _values

