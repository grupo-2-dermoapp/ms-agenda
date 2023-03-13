def test_service_is_alive(client):
    response = client.get("/dermoapp/agenda/v1/health")
    data = response.json
    assert "OK" == data['message']

    
