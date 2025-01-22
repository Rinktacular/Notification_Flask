from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notifications.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize DB
    db.init_app(app)
    socketio.init_app(app)

    # Initialize API
    api = Api(app)

    # Add Flask-RESTful resources
    from .routes import initialize_routes
    initialize_routes(api)

    from .sockets import NotificationNamespace
    socketio.on_namespace(NotificationNamespace("/notifications"))

    # Log all registered routes
    print("Registered Routes:")
    for rule in app.url_map.iter_rules():
        print(rule)

    return app
