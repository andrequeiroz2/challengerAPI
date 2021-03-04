from flask import request, Response
from flask_restful import Resource
from controller.controller_task import (
    one_task,
    all_task,
    create_task,
    update_task,
    delete_task,
    get_state,
)
from message.msg import ADD_TASK_SUCCESS, UPDATE_TASK_SUCCESS, DELETE_TASK_SUCCESS
from mongoengine.errors import (
    FieldDoesNotExist,
    NotUniqueError,
    DoesNotExist,
    ValidationError,
    InvalidQueryError,
)
from error.errors import (
    DeletingTaskError,
    SchemaValidationError,
    TaskAlreadyExistsError,
    InternalServerError,
    UpdatingTaskError,
    TaskNotExistsError,
    TaskNotRegistered,
)


class TaskApi(Resource):
    def get(self):
        tasks = all_task()
        if (len(tasks) == 2) or (tasks is None):
            raise TaskNotRegistered
        else:
            return Response(tasks, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            create_task(**body)
            return {"msg": ADD_TASK_SUCCESS, "task_name": body["task_name"]}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise TaskAlreadyExistsError
        except Exception:
            raise InternalServerError


class TasksApi(Resource):
    def get(self, name):
        try:
            task = one_task(name)
            return Response(task, mimetype="application/json", status=200)
        except DoesNotExist:
            raise TaskNotExistsError
        except Exception:
            raise InternalServerError

    def put(self, name):
        try:
            body = request.get_json()
            update_task(name, body)
            return {"msg": UPDATE_TASK_SUCCESS}, 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingTaskError
        except NotUniqueError:
            raise TaskAlreadyExistsError
        except Exception:
            raise InternalServerError

    def delete(self, name):
        try:
            delete_task(name)
            return {"msg": DELETE_TASK_SUCCESS}, 200
        except DoesNotExist:
            raise DeletingTaskError
        except Exception:
            raise InternalServerError


class TasksApiState(Resource):
    def get(self, state):
        try:
            task = get_state(state)
            return Response(task, mimetype="application/json", status=200)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise TaskNotExistsError
        except Exception:
            raise InternalServerError


def get(self):
    tasks = all_task()
    if (len(tasks) == 2) or (tasks is None):
        raise TaskNotRegistered
    else:
        return Response(tasks, mimetype="application/json", status=200)
