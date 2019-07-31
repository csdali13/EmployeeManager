# empManager/emp_records/__init__.py

from flask import Blueprint

emp_record_blueprint = Blueprint('emp_record_blueprint', __name__, template_folder='templates')

from empManager.emp_records import routes, models  # to avoid circular imports
