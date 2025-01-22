from flask import request
from flask_restful import Resource
from . import db, socketio
from .models import Notification

class NotificationResource(Resource):
    def get(self):
        notifications = Notification.query.all()
        return [n.to_dict() for n in notifications]

    def post(self):
        data = request.get_json()
        new_notification = Notification(
            title=data["title"],
            message=data["message"]
        )
        db.session.add(new_notification)
        db.session.commit()

        # Emit notification in real-time
        socketio.emit("new_notification", new_notification.to_dict(), namespace="/notifications")

        return {"message": "Notification created", "notification": new_notification.to_dict()}, 201

def initialize_routes(api):
    print("Registering /notifications route")
    api.add_resource(NotificationResource, "/notifications")