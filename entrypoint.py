from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from app import create_app
from flask import jsonify
from flask_migrate import Migrate
from app.views.views import Health, DoctorView, PatientView
from app.views.views import AgendaByDoctorView, EventView
from app.views.views import EventbyIdView
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

api.add_resource(Health, "/dermoapp/agenda/v1/health")
api.add_resource(DoctorView, "/dermoapp/agenda/v1/doctors")
api.add_resource(PatientView, "/dermoapp/agenda/v1/patients")
api.add_resource(AgendaByDoctorView, "/dermoapp/agenda/v1/agenda/<string:doctor_uuid>")
api.add_resource(EventView, "/dermoapp/agenda/v1/events")
api.add_resource(EventbyIdView, "/dermoapp/agenda/v1/events/<string:event_uuid>")

if __name__ == '__main__':
    app.run()