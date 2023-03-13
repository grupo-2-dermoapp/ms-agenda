from app.models.models import Doctor, Patient
from app.utils.utils import uuid4Str

def test_create_event_with_bad_data(client):
    payload = {}
    payload['doctor_uuid'] = ''
    payload['pacient_uuid'] = ''
    response = client.post("/dermoapp/agenda/v1/events", json=payload)
    data = response.json
    code = response.status
    assert data['message'] == 'No se pudo registrar el evento'
    assert code == '400 BAD REQUEST'

def test_create_event_with_valid_data(client, app):
    doctor = create_doctor(client)
    patient = create_patient(client)
    
    payload = {}
    payload['doctor_uuid'] = doctor['uuid']
    payload['patient_uuid'] = patient['uuid']
    print(payload)
    response = client.post("/dermoapp/agenda/v1/events", json=payload)
    data = response.json
    code = response.status
    print(data)
    print(code)
    assert data['message'] == 'No se pudo registrar el evento'
    assert code == '400 BAD REQUEST'


def create_doctor(client):
    payload = {}
    payload['uuid'] = uuid4Str()
    payload['location'] = 'test'
    response = client.post("/dermoapp/agenda/v1/doctors", json=payload)
    print(response.status)
    if (response.status == '201 CREATED'):
        return payload
    else:
        return {}


def create_patient(client):
    payload = {}
    payload['uuid'] = uuid4Str()
    payload['location'] = 'test'
    response = client.post("/dermoapp/agenda/v1/patients", json=payload)
    print(response.status)
    if (response.status == '201 CREATED'):
        return payload
    else:
        return {}
    