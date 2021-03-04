from api_init.api_task import TaskApi, TasksApi, TasksApiState


def init_routes_task(api):
    api.add_resource(TaskApi, "/api/tasks")
    api.add_resource(TasksApi, "/api/tasks/<name>")
    api.add_resource(TasksApiState, "/api/tasks/state/<state>")
