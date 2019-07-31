# from flask_sqlalchemy import SQLAlchemy
# import os, sys
# from flask import Flask

# empManager_db = SQLAlchemy()   # need to pass the flask main instance to this db

# def create_app(config_type):
#     app = Flask(__name__)
#     configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
#     app.config.from_pyfile(configuration)
#     empManager_db.init_app(app)

#     from empManager.emp_records import emp_record_blueprint

#     app.register_blueprint(emp_record_blueprint) 


#     return app


# if __name__ == '__main__':
#     flask_app = create_app('dev')

#     with flask_app.app_context():
#         empManager_db.create_all()

#     flask_app.run()


from empManager import create_app, empManager_db  # from the app package __init__

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        empManager_db.create_all()
    flask_app.run()



