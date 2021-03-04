import unittest
import os
import json
from database.db import db
from app import app


user = json.dumps({"user_name": "valmir"})


class UserTestCase(unittest.TestCase):
    """
    This class represents the user test case
    """

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def test_api_add_user(self):
        """
        Add users
        """
        res = self.app.post(
            "/api/users", headers={"Content-Type": "application/json"}, data=user
        )
        self.assertEqual(res.status_code, 200)

    def test_api_getAll_user(self):
        """
        Get all users
        """
        user_all = json.dumps({"user_name": "andre"})
        res = self.app.post(
            "/api/users", headers={"Content-Type": "application/json"}, data=user_all
        )
        self.assertEqual(res.status_code, 200)
        res = self.app.get("/api/users", headers={"Content-Type": "application/json"})
        self.assertEqual(res.status_code, 200)

    def test_api_getOne_user(self):
        """
        Get one users
        """
        user_one = json.dumps({"user_name": "one_user"})
        rv = self.app.post(
            "/api/users", headers={"Content-Type": "application/json"}, data=user_one
        )
        self.assertEqual(rv.status_code, 200)

        result_in_json = json.loads(rv.data.decode("utf-8").replace("'", '"'))
        res = self.app.get(
            "/api/users/{}".format(result_in_json["user_name"]),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(res.status_code, 200)

    def test_api_update_user(self):
        """
        Update users
        """
        user = json.dumps({"user_name": "user_one"})

        rv = self.app.post(
            "/api/users", headers={"Content-Type": "application/json"}, data=user
        )
        self.assertEqual(rv.status_code, 200)

        rv = self.app.put(
            "/api/users/user_one",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"user_name": "user_up"}),
        )
        self.assertEqual(rv.status_code, 200)

    def test_api_delete_user(self):
        """
        Delete users
        """
        user = json.dumps({"user_name": "user_delete"})
        rv = self.app.post(
            "/api/users", headers={"Content-Type": "application/json"}, data=user
        )
        self.assertEqual(rv.status_code, 200)

        res = self.app.delete(
            "/api/users/user_delete", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

        result = self.app.get(
            "/api/users/user_delete", headers={"Content-Type": "application/json"}
        )
        self.assertEqual(result.status_code, 400)

    def tearDown(self):
        """
        Delete Database collections after the test is complete
        """
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)


if __name__ == "__main__":
    unittest.main()
