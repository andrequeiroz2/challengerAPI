# general error
class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


# erros user
class UserAlreadyExistsError(Exception):
    pass


class UpdatingUserError(Exception):
    pass


class UserNotExistsError(Exception):
    pass


class UserNotRegistered(Exception):
    pass


# errors task
class TaskAlreadyExistsError(Exception):
    pass


class UpdatingTaskError(Exception):
    pass


class TaskNotExistsError(Exception):
    pass


class DeletingTaskError(Exception):
    pass


class TaskNotRegistered(Exception):
    pass


errors = {
    "InternalServerError": {"message": "Something went wrong", "status": 500},
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400,
    },
    "UserAlreadyExistsError": {
        "message": "User with given name already exists",
        "status": 400,
    },
    "UpdatingUserError": {
        "message": "Updating user added by other is forbidden",
        "status": 403,
    },
    "UserNotExistsError": {
        "message": "User with given name doesn't exists",
        "status": 400,
    },
    "TaskAlreadyExistsError": {
        "message": "Task with given name already exists",
        "status": 400,
    },
    "UpdatingTaskError": {
        "message": "Updating task added by other is forbidden",
        "status": 403,
    },
    "TaskNotExistsError": {
        "message": "Task with given name doesn't exists",
        "status": 400,
    },
    "DeletingTaskError": {
        "message": "Task with given id doesn't exists",
        "status": 400,
    },
    "TaskNotRegistered": {"message": "Not any tasks registered", "status": 400},
    "UserNotRegistered": {"message": "Not any users registered", "status": 400},
}
