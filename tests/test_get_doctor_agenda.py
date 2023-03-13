from app.models.models import Doctor

def test_get_agenda_with_bad_doctor_id(client):
    uuid_doctor = 'test'
    response = client.get("/dermoapp/agenda/v1/agenda/{}".format(uuid_doctor))
    data = response.json
    code = response.status
    print(data)
    print(code)
    assert data['Message'] == 'No existe una agenda'
    assert code == '400 BAD REQUEST'

# def get_agenda_with_valid_doctor_id(client, app):
#     doctor = create_doctor(app)
#     uuid_doctor = doctor.uuid
#     response = client.post("/dermoapp/agenda/v1/agenda/{}".format(uuid_doctor), json={})
#     data = response.json
#     code = response.status
#     assert data['message'] == 'Agenda por uuid de doctor'
#     assert code == '200 OK'

# def create_doctor(app):
#     with app.app_context():
#         doctor = Doctor(
#             location = 'test'
#         )
#         db.session.add(doctor)
#         db.session.commit()
#         db.session.close()
#         return doctor