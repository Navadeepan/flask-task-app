from flask import Flask

from config import SQLALCHEMY_DATABASE_URI
from dbconfig import db
from routes import generate_routes


def create_app():
    main_app = Flask(__name__)

    # Set debug true for catching the errors.
    main_app.config['DEBUG'] = True

    # Set database url.
    main_app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    main_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    generate_routes(main_app)

    # Database initialize with app.
    db.init_app(main_app)
    # Create all database tables inside the app context.
    with main_app.app_context():
        db.create_all()

    # Return app.
    return main_app


if __name__ == '__main__':
    # Create app.
    app = create_app()

    # Run app. For production use another web server.
    # Set debug and use_reloader parameters as False.
    app.run(port=5000, debug=True, host='localhost', use_reloader=True)
