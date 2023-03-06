# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
from app.models.models import Patient, Doctor, Agenda, Event, db
from app.models.models import AgendaSchema, EventSchema
from sqlalchemy.exc import IntegrityError
import requests
import datetime
import os


class Health(Resource):
    def get(self):
        data = {
            "message" : "OK"
        }
        return data, 200

class DoctorView(Resource):
    def post(self):
        request_data = request.json
        try:
            doctor =  Doctor(
                uuid = request_data['uuid'],
                location = request_data['location']
            )
            agenda = Agenda(
                doctor_uuid = doctor.uuid
            )
            db.session.add(doctor)
            db.session.add(agenda)
            db.session.commit()
            data = {
                "message" : "OK"
            }
            return data, 201
        except IntegrityError as e:
            data = {
                "message" : "fail"
            }
            return data, 400 
        finally:
            db.session.close()

class PatientView(Resource):
    def post(self):
        request_data = request.json
        try:
            patient =  Patient(
                uuid = request_data['uuid'],
                location = request_data['location']
            )
            db.session.add(patient)
            db.session.commit()
            data = {
                "message" : "OK"
            }
            return data, 201
        except IntegrityError:
            data = {
                "message" : "fail"
            }
            return data, 400 
        finally:
            db.session.close()

class AgendaByDoctorView(Resource):
    def get(self, doctor_uuid):
        agenda = Agenda.query.filter_by(
            doctor_uuid = doctor_uuid
        ).first()

        if agenda:
            data = {
                "code" : "",
                "message" : "Agenda por uuid de doctor",
                "agenda" : AgendaSchema().dump(agenda)
            }
            return data, 200
        else:
            data = {
                "code" : "",
                "Message" : "No existe una agenda"
            }
            return data, 400
        
class EventView(Resource):
    def post(self):
        request_data = request.json
        try:
            doctor_uuid = request_data['doctor_uuid']
            patient_uuid = request_data['patient_uuid']
            patient = db.session.query(Patient).filter(
                Patient.uuid == patient_uuid).first()
            agenda = Agenda.query.filter_by(
                doctor_uuid = doctor_uuid
            ).first()
            now = datetime.datetime.now()
            possible_start_date = now - datetime.timedelta(
                minutes=now.minute,
                seconds=now.second,
                microseconds=now.microsecond)\
            + datetime.timedelta(days=1)
        
            if agenda.events:
                recent_event = Event.query.filter(
                                    Event.start_date >= datetime.datetime.now())\
                                    .order_by(Event.start_date.desc())\
                                    .first()
                
                if possible_start_date > recent_event.start_date:
                    start_date = possible_start_date
                else:
                    start_date = recent_event.start_date + datetime.timedelta(hours=1)
            else:        
                start_date = possible_start_date

            patient_request_response = requests.get(
                os.getenv('AUTH_SERVICE')+str(patient.location))
            
            if patient_request_response.status_code == 200:
                patient_info = patient_request_response.json()
                event_name = "Evento con "+ str(patient_info["names"])
            else:
                event_name = "Evento con paciente"

            event = Event(
                name = event_name,
                start_date = start_date,
                patient_uuid = patient_uuid,
                doctor_uuid = doctor_uuid,
                agenda_uuid = agenda.uuid
            )

            db.session.add(event)
            db.session.commit()

            data = {
                "code" : "",
                "message" : "Evento agregado correctamente",
                "event" : EventSchema().dump(event)
            }

            return data, 201 
        
        except:
            data = {
                "code" : "",
                "message" : "No se pudo registrar el evento"
            }

            return data, 400 

class EventbyIdView(Resource):
    def get(self, event_uuid):
        event = Event.query.filter_by(
            uuid = event_uuid
        ).first()

        if event:
            data = {
                "code" : "",
                "message" : "Evento por uuid",
                "event" : EventSchema().dump(event)
            }

            return data, 200
        
        else:
            data = {
                "code" : "",
                "message" : "Evento no encontrado"
            }

            return data, 400
