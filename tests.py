import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

# Test ID: T1
# Description: Test the index page returns the correct HTTP status code and uses the correct template
@pytest.mark.parametrize("path, expected_template", [
    ("/", "index.html"),
    ("/index", "index.html"),
])
def test_index_page(client, path, expected_template):
    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 200
    assert expected_template in str(response.data)

# Test ID: T2
# Description: Test the contacts page returns the correct HTTP status code and uses the correct template
def test_contacts_page(client):
    # Act
    response = client.get("/contacts")

    # Assert
    assert response.status_code == 200
    assert "contacts.html" in str(response.data)

# Test ID: T3
# Description: Test for non-existent routes
@pytest.mark.parametrize("path", [
    ("/nonexistent"),
    ("/404"),
    ("/null")
])
def test_404_pages(client, path):
    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 404

# Test ID: T4
# Description: Test the server's response to method not allowed
@pytest.mark.parametrize("path, method", [
    ("/", "POST"),
    ("/index", "PUT"),
    ("/contacts", "DELETE")
])
def test_method_not_allowed(client, path, method):
    # Act
    response = client.open(path, method=method)

    # Assert
    assert response.status_code == 405

# Test ID: T5
# Description: Test the application's response to unexpected input types in the URL
@pytest.mark.parametrize("path", [
    ("/index<script>alert('hack')</script>"),
    ("/contacts<script>alert('hack')</script>")
])
def test_unexpected_input_types(client, path):
    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 404
