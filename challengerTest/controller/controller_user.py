from database.db import db
from model.model_user import User


def all_user():
    user = User.objects().to_json()
    return user


def one_user(name: str):
    user = User.objects.get(user_name=name).to_json()
    return user


def create_user(user_name: str):
    User(user_name=user_name).save()


def update_user(name: str, body):
    User.objects.get(user_name=name).update(**body)


def get_user_for_task(name: str):
    user = User.objects.get(user_name=name)
    return user


def delete_user(name: str):
    User.objects(user_name=name).delete()
