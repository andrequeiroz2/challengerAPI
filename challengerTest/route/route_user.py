from api_init.api_user import UserApi, UsersApi


def init_routes_user(api):
    api.add_resource(UserApi, "/api/users")
    api.add_resource(UsersApi, "/api/users/<name>")
