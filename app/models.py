from . import db

class Notification(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  message = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime, default=db.func.now())

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "message": self.message,
      "crated_at": self.created_at.isoformat() if self.created_at else None
    }