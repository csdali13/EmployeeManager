from empManager.emp_records import emp_record_blueprint
from empManager.emp_records.models import Employee, Department
from flask import render_template, request, redirect, flash, url_for
from empManager.emp_records.addEmployeeForm import AddEmployeeForm
from empManager import empManager_db  
import sys


@emp_record_blueprint.route('/')
def emp_list():
    emps = Employee.query.all()
    return render_template('home.html', emps=emps)


@emp_record_blueprint.route('/add/addemployeeform', methods = ['GET', 'POST'])
def add_employee_popupform():
    form = AddEmployeeForm()
#    print('name: ' + form.name.data, file=sys.stdout)
    if (request.method == 'POST'):
        Employee.create_employee(
            name = form.name.data,
            designation = form.designation.data,
            address = form.address.data,
            phone = form.phone.data,
            department_id = form.department_id.data)
        flash('Employee added successfully')
        return redirect(url_for('emp_record_blueprint.emp_list'))
  #  else:
    #print('Error in adding employee', file=sys.stderr)

    return render_template('addEmployee.html', form=form)

@emp_record_blueprint.route('/display/department/<department_id>')
def display_department(department_id):
    department = Department.query.filter_by(id=department_id).first()
    department_employees = Employee.query.filter_by(department_id = department.id).all()

    return render_template('department.html', department=department, department_employees=department_employees)


@emp_record_blueprint.route('/delete/deleteemployee/<emp_id>', methods=['GET', 'POST'])
def delete_employee(emp_id):
    print(emp_id, file=sys.stdout)
    print('Inside delete employee method: emp id', file=sys.stdout)
    emp = Employee.query.get(emp_id)
    if request.method == 'POST':
        empManager_db.session.delete(emp)
        empManager_db.session.commit()
        flash.message('Employee deleted successfully')
        print('Emp deleted', file=sys.stdout)
    return redirect(url_for('emp_record_blueprint.emp_list'))
