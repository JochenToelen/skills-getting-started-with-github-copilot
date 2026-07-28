def test_get_activities_returns_success(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_expected_shape(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert isinstance(payload, dict)
    assert "Chess Club" in payload

    activity = payload["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity


def test_get_activities_participants_is_a_list(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    for details in payload.values():
        assert isinstance(details["participants"], list)