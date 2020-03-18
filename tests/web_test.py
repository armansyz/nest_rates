import base64
import json
import pytest
from .context import web


@pytest.fixture(scope='module')
def client():
    client = web.app.test_client()
    yield client


def test_service_success(client):
    """Test whether the service works correctly
    """
    url = '/nest?nkeys=country'

    mock_request_headers = {
        'Authorization': 'Basic ' + base64.b64encode(
            bytes('user' + ":" + 'user', 'ascii')).decode('ascii')
    }

    mock_request_data = [
        {
            'country': 'ES',
            'city': 'Madrid',
            'currency': 'EUR',
            'amount': '100'
        }
    ]

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 200


def test_service_failure(client):
    """Test whether the service works correctly
    """
    url = '/nest?nkeys=country'

    mock_request_headers = {
        'Authorization': 'Basic ' + base64.b64encode(
            bytes('test' + ":" + 'user', 'ascii')).decode('ascii')
    }

    mock_request_data = [
        {
            'country': 'ES',
            'city': 'Madrid',
            'currency': 'EUR',
            'amount': '100'
        }
    ]

    response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    assert response.status_code == 401
