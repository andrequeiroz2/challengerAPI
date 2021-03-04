from flask import request, Response
from flask_restful import Resource
from model.model_user import User
from controller.controller_user import (
    one_user,
    all_user,
    create_user,
    update_user,
    delete_user,
)
from message.msg import ADD_USER_SUCCESS, UPDATE_USER_SUCCESS, DELETE_USER_SUCCESS
from mongoengine.errors import (
    FieldDoesNotExist,
    NotUniqueError,
    DoesNotExist,
    ValidationError,
    InvalidQueryError,
)
from error.errors import (
    SchemaValidationError,
    UserAlreadyExistsError,
    InternalServerError,
    UpdatingUserError,
    UserNotExistsError,
    UserNotRegistered,
)


class UserApi(Resource):
    def get(self):
        users = all_user()
        if (len(users) == 2) or (users is None):
            raise UserNotRegistered
        else:
            return Response(users, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            create_user(**body)
            return {"msg": ADD_USER_SUCCESS, "user_name": body["user_name"]}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except ValidationError:
            raise SchemaValidationError
        except NotUniqueError:
            raise UserAlreadyExistsError
        except Exception:
            raise InternalServerError


class UsersApi(Resource):
    def get(self, name):
        try:
            user = one_user(name)
            return Response(user, mimetype="application/json", status=200)
        except DoesNotExist:
            raise UserNotExistsError
        except Exception:
            raise InternalServerError

    def put(self, name):
        try:
            body = request.get_json()
            update_user(name, body)
            return {"msg": UPDATE_USER_SUCCESS}, 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingUserError
        except NotUniqueError:
            raise UserAlreadyExistsError
        except Exception:
            raise InternalServerError

    def delete(self, name):
        try:
            delete_user(name)
            return {"msg": DELETE_USER_SUCCESS}, 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingUserError
        except Exception:
            raise InternalServerError
