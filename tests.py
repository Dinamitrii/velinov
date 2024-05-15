import pytest
from app import app as flask_app

@pytest.fixture
def app():
    print("Debugging: Inside fixture - app")
    yield flask_app
    print("Debugging: Exiting fixture - app")

@pytest.fixture
def client(app):
    print("Debugging: Inside fixture - client")
    result = app.test_client()
    print("Debugging: Exiting fixture - client")
    return result

# Test ID: T1
# Description: Test the index page returns the correct HTTP status code and uses the correct template
@pytest.mark.parametrize("path, expected_template", [
    ("/", "index.html"),
    ("/index", "index.html"),
])
def test_index_page(client, path, expected_template):
    # Act
    print(f"Debugging: Path - {path}")
    print(f"Debugging: Expected Template - {expected_template}")
    response = client.get(path)

    # Assert
    assert response.status_code == 200
    assert expected_template in str(response.data)

# Test ID: T2
# Description: Test the contacts page returns the correct HTTP status code and uses the correct template
def test_contacts_page(client):
    # Act
    print("Debugging: Testing contacts page")
    response = client.get("/contacts")
    print(f"Debugging: Response status code - {response.status_code}")

    # Assert
    assert response.status_code == 200
    assert "contacts.html" in str(response.data)
    print("Debugging: Contacts page test completed")

# Test ID: T3
# Description: Test for non-existent routes
@pytest.mark.parametrize("path", [
    ("/nonexistent"),
    ("/404"),
    ("/null")
])
def test_404_pages(client, path):
    # Act
    print("Debugging: Testing 404 pages")
    print(f"Debugging: Path - {path}")
    response = client.get(path)
    print(f"Debugging: Response status code - {response.status_code}")

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
    print(f"Debugging: Testing method not allowed - Path: {path}, Method: {method}")
    response = client.open(path, method=method)
    print(f"Debugging: Response status code - {response.status_code}")

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
    print(f"Debugging: Testing unexpected input types - Path: {path}")
    response = client.get(path)
    print(f"Debugging: Response status code - {response.status_code}")

    # Assert
    assert response.status_code == 404
