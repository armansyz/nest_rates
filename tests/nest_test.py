import typing
import io
import pytest
import json

from .context import nest


@pytest.fixture()
def setup_valid_json_data(monkeypatch):
    """Prepare valid json for tests"""
    monkeypatch.setattr('sys.stdin', io.StringIO('[{"country": "US", "amount": 100 }, {"country": "ES", "amount": 120 '
                                                 '}]'))


@pytest.fixture()
def setup_invalid_json_data(monkeypatch):
    """Prepare bad json for tests"""
    monkeypatch.setattr('sys.stdin', io.StringIO('["country": "US", "amount": 100 }]'))


def test_valid_json(setup_valid_json_data):
    """Test whether read_json() returns valid json
    """
    assert isinstance(nest.read_json(), (typing.List, typing.Dict))


def test_bad_json(setup_invalid_json_data):
    """Test whether read_json() raises a JSONDecoder on bad json
    """
    with pytest.raises(json.JSONDecodeError):
        nest.read_json()


def test_no_input():
    """Test whether read_json() raises an AttributeError on no input
    """
    with pytest.raises(AttributeError):
        nest.read_json()


def test_pass_keys():
    """Test whether nesting keys are correctly passed
    """
    parser = nest.parse_args('nesting_level_1 nesting_level_2 nesting_level_3'.split())
    assert isinstance(parser.nkeys, typing.List)


def test_return_valid_json(setup_valid_json_data):
    """Test whether program returns a valid json
    """
    json_data = nest.read_json()
    assert isinstance(nest.nest_json(json_data, None), (typing.List, typing.Dict))


def test_array_nesting(setup_valid_json_data):
    """Test whether nest_array() correctly processes an array
    """
    json_data = nest.read_json()
    nkey = 'country'
    assert len({x[nkey] for x in json_data}) == len(nest.nest_array(json_data, nkey))


def test_key_error_exception(setup_valid_json_data):
    """Test whether nest_json() raises a KeyError exception on non-existing key
    """
    json_data = nest.read_json()
    nkeys = ['country', 'info']
    with pytest.raises(KeyError):
        nest.nest_json(json_data, nkeys)


