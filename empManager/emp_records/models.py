from empManager import empManager_db
import sys

class Department(empManager_db.Model):
    __tablename__ = 'department'

    id = empManager_db.Column(empManager_db.Integer, primary_key = True)
    name = empManager_db.Column(empManager_db.Integer)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return repr((self.name, self.id))

    def add_department(self, depToAdd):
        empManager_db.session.add_all([depToAdd])
        empManager_db.session.commit()


class Employee(empManager_db.Model):
    __tablename__ = 'employee'

    id = empManager_db.Column(empManager_db.Integer, primary_key=True)
    name = empManager_db.Column(empManager_db.String(200), nullable=False)
    designation = empManager_db.Column(empManager_db.String(80), nullable=False)
    address = empManager_db.Column(empManager_db.String(400))
    phone = empManager_db.Column(empManager_db.Integer)
    department_id = empManager_db.Column(empManager_db.Integer, empManager_db.ForeignKey('department.id'))

    def __init__(self, name,  designation, address, phone, department_id):
        self.name = name
        self.designation = designation
        self.address = address
        self.phone = phone
        self.department_id = department_id

    def __repr__(self):
        return repr((self.name, self.id, self.designation))

    @classmethod
    def create_employee(cls, name, designation, address, phone, department_id):
        print('inside the create_employee in models.py', file=sys.stderr)
        emp = cls(name=name, designation =designation, address = address, phone = phone, department_id = department_id)
        empManager_db.session.add(emp)
        empManager_db.session.commit()
        print('db committed', file=sys.stderr)

