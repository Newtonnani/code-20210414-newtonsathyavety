from . import db
import datetime

class Bmi(db.Model):
    __tablename__ = 'bmi_details'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    gender = db.Column(db.String(100),nullable=False)
    height_cm = db.Column(db.Integer,nullable=False)
    weight_kg = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'Gender': self.gender,
            'HeightCm': self.height_cm,
            'WeightKg':self.weight_kg
        }