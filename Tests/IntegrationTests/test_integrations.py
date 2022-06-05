import pytest

from App import create_app
import flask
from sqli_app_db import createDB


@pytest.fixture(scope="session", autouse=True)
def create_test_database(tmp_path_factory):
    tmp_dir = tmp_path_factory.mktemp("tmp")
    database_filename = tmp_dir / "test_database.db"
    createDB(database_filename)


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.secret_key = 'FlaskSecret'
    app.config.update({"TESTING": True, })
    testing_client = app.test_client(use_cookies=True)
    context = app.app_context()
    context.push()
    yield testing_client
    context.pop()


def test_register(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b'Please sign Up'
    # When
    response = test_client.get('/register')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data


def test_login_page(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b'Please sign In'
    # When
    response = test_client.get('/signin')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data


def test_signin_fail(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b'Wrong Credentials! Please check again'
    credentials = {
        "username": "no",
        "password": "no"
    }
    # When
    response = test_client.post('/signin', data=credentials)
    print(response.data)
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_alert in response.data


def test_signin_success(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b'Connected'
    credentials = {
        "username": "admin",
        "password": "admin"
    }
    print(credentials)
    # When
    response = test_client.post('/signin', data=credentials, follow_redirects=True)
    print(response.data)
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_alert in response.data


def test_logout(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b'Logged out'
    with test_client.session_transaction() as session:
        session['logged_in'] = True
        session['username'] = "admin"
    # When
    response = test_client.get('/logout', follow_redirects=True)
    print(response.data)
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_alert in response.data


def test_notes(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b'My Notes'
    with test_client.session_transaction() as session:
        session['logged_in'] = True
        session['username'] = "admin"
    # When
    response = test_client.get('/')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data


def test_create_note_page(test_client):
    # Given
    expected_status_code = 200
    expected_page_title = b"Add note"
    with test_client.session_transaction() as session:
        session['logged_in'] = True
        session['username'] = "admin"
    # When
    response = test_client.get('/create')
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_title in response.data


def test_Note_add(test_client):
    # Given
    expected_status_code = 200
    expected_page_alert = b"Note added"
    note_add = {
        "title": "test",
        "note": "test",
    }
    with test_client.session_transaction() as session:
        session['logged_in'] = True
        session['username'] = "admin"
    # When
    response = test_client.post('/insert', data=note_add, follow_redirects=True)
    # Then
    assert expected_status_code == response.status_code
    assert expected_page_alert in response.data


