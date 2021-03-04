from mongoengine.base.fields import ObjectIdField
from database.db import db
from model.model_task import Task


def all_task():
    task = Task.objects().to_json()
    return task


def one_task(name: str):
    task = Task.objects.get(task_name=name).to_json()
    return task


def create_task(task_name: str, task_desc: str, user_send: str):
    Task(
        task_name=task_name,
        task_desc=task_desc,
        user_send=user_send,
    ).save()


def update_task(name: str, body):
    Task.objects.get(task_name=name).update(**body)


def delete_task(name: str):
    Task.objects(task_name=name).delete()


def get_state(state):
    task = Task.objects.filter(task_state=state).to_json()
    return task
