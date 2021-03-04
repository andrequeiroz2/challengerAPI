import unittest
import os
import json
from app import app
from database.db import db


task0 = json.dumps(
    {"task_name": "servidor", "task_desc": "error", "user_send": "andre"}
)

task1 = json.dumps(
    {"task_name": "email", "task_desc": "desable", "user_send": "valmir"}
)


class TaskTestBase(unittest.TestCase):
    """
    This class represents the task test case
    """

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def test_api_add_task(self):
        """
        Add task
        """
        res = self.app.post(
            "/api/tasks", headers={"Content-Type": "application/json"}, data=task0
        )
        self.assertEqual(res.status_code, 200)

        res = self.app.get("/api/tasks", headers={"Content-Type": "application/json"})
        self.assertEqual(res.status_code, 200)

    def test_api_getAll_user(self):
        """
        Get all task
        """
        res = self.app.post(
            "/api/tasks", headers={"Content-Type": "application/json"}, data=task1
        )
        self.assertEqual(res.status_code, 200)

        res = self.app.get("/api/tasks", headers={"Content-Type": "application/json"})
        self.assertEqual(res.status_code, 200)

    def test_api_getOne_task(self):
        """
        Get one task
        """
        task_one = json.dumps(
            {
                "task_name": "emailOne",
                "task_desc": "desableOne",
                "user_send": "valmirOne",
            }
        )

        rv = self.app.post(
            "/api/tasks", headers={"Content-Type": "application/json"}, data=task_one
        )
        self.assertEqual(rv.status_code, 200)

        result_in_json = json.loads(rv.data.decode("utf-8").replace("'", '"'))
        res = self.app.get(
            "/api/tasks/{}".format(result_in_json["task_name"]),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(res.status_code, 200)

    def test_api_getState_task(self):
        """
        Get state task
        """
        task_open = json.dumps(
            {
                "task_name": "stateOpen",
                "task_desc": "desableOne",
                "user_send": "valmirOne",
            }
        )
        res = self.app.post(
            "/api/tasks", headers={"Content-Type": "application/json"}, data=task_open
        )
        self.assertEqual(res.status_code, 200)

        rs = self.app.get(
            "/api/tasks/state/open", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(rs.status_code, 200)

    def test_api_update_task(self):
        """
        Update task
        """
        task2 = json.dumps(
            {
                "task_name": "flask",
                "task_desc": "flask-mongoengine",
                "user_send": "andre",
            }
        )

        task2_up = json.dumps(
            {
                "task_name": "flask",
                "task_desc": "flask-api",
                "task_state": "close",
                "user_send": "valmir",
            }
        )

        res = self.app.post(
            "/api/tasks", headers={"Content-Type": "application/json"}, data=task2
        )
        self.assertEqual(res.status_code, 200)

        rs = self.app.put(
            "/api/tasks/flask",
            headers={"Content-Type": "application/json"},
            data=task2_up,
        )
        self.assertEqual(rs.status_code, 200)

    def test_api_delete_task(self):
        """
        Delete tasks
        """
        task3 = json.dumps(
            {"task_name": "router", "task_desc": "default-router", "user_send": "admin"}
        )

        res = self.app.post(
            "/api/tasks", headers={"Content-Type": "application/json"}, data=task3
        )
        self.assertEqual(res.status_code, 200)

        rv = self.app.delete(
            "/api/tasks/router", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(rv.status_code, 200)

        rg = self.app.get("/api/tasks", headers={"Content-Type": "application/json"})
        self.assertEqual(rg.status_code, 400)

    def tearDown(self):
        """
        Delete Database collections after the test is complete
        """
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)


if __name__ == "__main__":
    unittest.main()
