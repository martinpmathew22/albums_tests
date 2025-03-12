import requests
from http import HTTPStatus

def test_get_albums_by_id():
    url = "http://127.0.0.1:8080/albums/1"  # Replace with your mock API URL
    response = requests.get(url)

    # Verify status code
    assert response.status_code == HTTPStatus.OK

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Verify response structure (Assuming a book object with 'id', 'title', and 'author')
    data = response.json()  
    assert isinstance(data, dict)
    assert "id" in data
    assert "title" in data
    assert "artist" in data

def test_get_albums_by_id_negative_scenario():
    url = "http://127.0.0.1:8080/albums/100"  # Replace with your mock API URL
    response = requests.get(url)

    # Verify status code
    assert response.status_code == HTTPStatus.NOT_FOUND
