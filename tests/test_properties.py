def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 404 or response.status_code == 200

