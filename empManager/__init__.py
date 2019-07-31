# empManager/__init__.py
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
from flask_bootstrap import Bootstrap

empManager_db = SQLAlchemy()   # need to pass the flask main instance to this db
bootstrap = Bootstrap()

def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    empManager_db.init_app(app)
    bootstrap.init_app(app)

    from empManager.emp_records import emp_record_blueprint

    app.register_blueprint(emp_record_blueprint)

    return app

