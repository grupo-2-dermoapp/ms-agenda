from app.views.views import Health, DoctorView, PatientView
from app.views.views import AgendaByDoctorView, EventView
from app.views.views import EventbyIdView

from flask_restful import Api
from flask_cors import CORS
from app import create_app
from flask_migrate import upgrade
from app import db

import pytest

@pytest.fixture()
def app():

    # settings_module = os.getenv('APP_SETTINGS_MODULE')
    settings_module = 'config.develop.Test'
    app = create_app(settings_module)
    db.init_app(app)

    api = Api(app)
    CORS(app)

    api.add_resource(Health, "/dermoapp/agenda/v1/health")
    api.add_resource(DoctorView, "/dermoapp/agenda/v1/doctors")
    api.add_resource(PatientView, "/dermoapp/agenda/v1/patients")
    api.add_resource(AgendaByDoctorView, "/dermoapp/agenda/v1/agenda/<string:doctor_uuid>")
    api.add_resource(EventView, "/dermoapp/agenda/v1/events")
    api.add_resource(EventbyIdView, "/dermoapp/agenda/v1/events/<string:event_uuid>")
    
    # with app.app_context():
    #         upgrade()

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()