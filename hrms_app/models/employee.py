from sqlalchemy import func

from ..db import db


class Employee(db.Model):
    """
    create a model for Employee with the required variables. 
    """
    id = db.Column(db.String(48), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    joined_at = db.Column(db.DateTime, nullable = False)
    attendance_count = db.Column(db.INTEGER, nullable = False)
    in_time = db.Column(db.DateTime, nullable = False)
    out_time = db.Column(db.DateTime, nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    @staticmethod
    def get(employee_id):
        return Employee.query.get(employee_id)

    @staticmethod
    def get_all():
        """
            get all the values of the employee table.
        """
        return Employee.query.all()    
