from database.db import db
from flask_mongoengine.wtf import model_form
from model.model_user import User


class Task(db.Document):
    task_name = db.StringField(required=True, max_length=30, unique=True)
    task_desc = db.StringField(required=True, max_length=150)
    task_state = db.StringField(required=True, default="open")
    user_send = db.StringField(required=True, max_length=30)
