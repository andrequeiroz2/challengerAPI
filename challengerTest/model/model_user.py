from database.db import db
from flask_mongoengine.wtf import model_form


class User(db.Document):
    user_name = db.StringField(required=True, max_length=30, unique=True)

    def __repr__(self):
        return "<User: {}>".format(self.user_name)
