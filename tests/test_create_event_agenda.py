from app.models.models import Doctor, Patient

def create_event_with_bad_data(client):
    payload = {}
    payload['doctor_uuid'] = ''
    payload['pacient_uuid'] = ''
    response = client.post("/dermoapp/agenda/v1/events", json=payload)
    data = response.json
    code = response.status
    assert data['message'] == 'No se pudo registrar el evento'
    assert code == '400 BAD REQUEST'

def create_event_with_valid_data(client, app):
    doctor = create_doctor(app)
    patient = create_patient(app)
    
    payload = {}
    payload['doctor_uuid'] = doctor.uuid
    payload['pacient_uuid'] = patient.uuid
    response = client.post("/dermoapp/agenda/v1/events", json=payload)
    data = response.json
    code = response.status
    assert data['message'] == 'Evento agregado correctamente'
    assert code == '201 CREATED'

def create_doctor(app):
    with app.app_context():
        doctor = Doctor(
            location = 'test'
        )
        db.session.add(doctor)
        db.session.commit()
        db.session.close()
        return doctor
    
def create_patient(app):
    with app.app_context():
        patient = Patient(
            location = 'test'
        )
        db.session.add(patient)
        db.session.commit()
        db.session.close()
        return patient