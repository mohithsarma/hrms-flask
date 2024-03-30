import secrets
from datetime import datetime

from flask import abort, render_template, redirect, url_for, request
from flask.blueprints import Blueprint

from .. import db
from ..models.employee import Employee

blueprint = Blueprint('employee', __name__)


@blueprint.route('/<_id>')
def get(_id):
    """
        get the Details of employee depending on employee id.  
    """
    employee = Employee.get(_id)

    if not employee:
        abort(404)

    return render_template('employee.html', employee=employee), 200


@blueprint.route('/list')
def emp_list():
    """
    function to get the list of all the employees in the database.
    """

    emps_list = Employee.get_all()

    if not emps_list:
        return render_template('create_employee.html'), 200

    return render_template('employee_list.html', emps_list=emps_list), 200


@blueprint.route('/create')
def emp_create():
    """
        Create an employee using form
    """
    return render_template('create_employee.html'), 200


@blueprint.route('/', methods=['POST'])
def create():
    """
        Create an Entry in the database using the form from the User.
    """
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    designation = request.form.get('designation')
    department = request.form.get('department')
    joined_at_string = request.form.get('joined_at')
    joined_at = datetime.strptime(joined_at_string, '%Y-%m-%d')
    attendance_count = 1
    in_time = datetime.now()
    out_time = datetime.now()
    employee_id = secrets.token_urlsafe(32)

    employee = Employee(id=employee_id, name=name, email=email, address=address, designation=designation, department=department, joined_at=joined_at,
                        attendance_count=attendance_count, in_time=in_time, out_time=out_time
                        )

    with db.transaction():
        db.persist(employee)

    return redirect(url_for('employee.get', _id=employee_id))


@blueprint.route('/<_id>/delete', methods=['POST'])
def delete(_id):
    """
        Delete the Employee depending on the empployee id. 
    """
    employee = Employee.get(_id)

    if not employee:
        abort(404)

    with db.transaction():
        db.delete(employee)

    return redirect(url_for('employee.emp_list'))
