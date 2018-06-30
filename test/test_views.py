from http import HTTPStatus

import pytest
from test.conftest import get_field


def test_root(client, app):
    """
    tests the homepage of the app.

    :param flask.testing.FlaskClient client:
    :param Flask app:
    :return:
    """
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK.value
    assert b'Vehicle data processor' in response.data


@pytest.mark.parametrize('field,value,request_data', [
    ('make', 'RENAULT', 'VF1KMS40A36042123,KB,H1,RENAULT'),
    ('make', 'HONDA', 'SHSRE67507U001669,KB,H1,HONDA'),
    ('make', 'HONDA', 'JHMBE17407S200596,KB,H3,HONDA'),
])
def test_vehicle_csv_single(field, value, request_data, client, app):
    """
    :param str field:
    :param str value:
    :param str request_data:
    :param flask.testing.FlaskClient client:
    :param Flask app:
    :return:
    """

    response = client.post(
        '/vehicle/csv', content_type='plain/text', data=request_data)
    assert response.status_code == HTTPStatus.OK.value
    assert get_field(next(iter(response.json.get('data', []))), field) == value


@pytest.mark.parametrize('count,request_data', [
    (8, 'VF1KMS40A36042123,KB,H1,RENAULT\n'
        'SHSRE67507U001669,KB,H1,HONDA\n'
        'JHMBE17407S200596,KB,H3,HONDA\n'
        'VF36ERFJC21545586,KB,H1,PEUGEOT\n'
        'VF3LB9HCGES022011,VA,H1,PEUGEOT\n'
        'WVWZZZ9NZ7Y062120,VA,H3,VW\n'
        'WF0WXXGCDW6R41261,VA,H1,FORD\n'
        'WVWZZZ3CZEE062520,VA,H2,VOLKSWAGEN\n'),
])
def test_vehicle_csv_file(count, request_data, client, app):
    """
    :param str count:
    :param str request_data:
    :param flask.testing.FlaskClient client:
    :param Flask app:
    :return:
    """
    response = client.post(
        '/vehicle/csv', content_type='plain/text', data=request_data)

    assert response.status_code == HTTPStatus.OK.value
    assert len(response.json.get('data', [])) == count
