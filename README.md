## Using the following packages
- flask
- flask-restful
- flask-socketio (with eventlet for async support)
- flask-sqlalchemy

## Required packages
- pip install flask flask_RESTful flask_sqlalchemy flask_socketio

## Create DB (in terminal)
  from app import create_app, db
  from app.models import Notification
  
  app = create_app()
  with app.app_context():
      db.create_all()

## Run the application
- python run.py

## Create Notification using Postman
- METHOD: POST
- URL: http://127.0.0.1:5000/notifications
- Headers: Content-Type: application/json
- Body: {
    "title": "Test Notification",
    "message": "This is a test notification created using Postman."
  }

## Notification should appear in the DOM if the React app is running on the '/notifications' route
