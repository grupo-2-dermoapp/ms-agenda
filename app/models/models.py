from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, ForeignKey, String, DateTime, Numeric
from sqlalchemy import Enum
from datetime import datetime
from app.utils.utils import uuid4Str
from app import db, ma

class Agenda(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    doctor_uuid = Column(String(40), ForeignKey('doctor.uuid'), nullable=True)
    events = db.relationship('Event', backref='agenda', lazy=True)

class Event(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    name = Column(String(200))
    start_date = Column(DateTime)
    patient_uuid = Column(String(40), ForeignKey('patient.uuid'), nullable=False)
    doctor_uuid = Column(String(40), ForeignKey('doctor.uuid'), nullable=True)
    agenda_uuid = Column(String(40), ForeignKey('agenda.uuid'))
    
class Doctor(db.Model):
    uuid = Column(String(40), primary_key=True, nullable=False)
    location = Column(String(150), nullable=False)

class Patient(db.Model):
    uuid = Column(String(40), primary_key=True, nullable=False)
    location = Column(String(150), nullable=False)

class AgendaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Agenda
        load_instance = True
        include_relationships = True

class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        load_instance = True
        include_relationships = True