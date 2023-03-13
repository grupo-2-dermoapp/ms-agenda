def get_event_with_bad_id(client):
    uuid_test = 'test'
    response = client.get("/dermoapp/agenda/v1/events/{}".format(uuid_test))
    data = response.json
    code = response.status
    assert data['message'] == 'Evento no encontrado'
    assert code == '400 BAD REQUEST'