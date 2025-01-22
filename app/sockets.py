from flask_socketio import Namespace, emit

class NotificationNamespace(Namespace):
  def on_connect(self):
    print("Client connected")

  def on_disconnect(self):
    print("Client disconnected")

  def on_message(self, message):
    print("Received message:", message)
    emit("response", {"message": "Message receieved!"})