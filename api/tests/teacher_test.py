import unittest
import json
from ..main import app, db



class TeacherTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.create_all()

    def test(self):
        # Given
        payload = json.dumps({
            "name": "dean@gmail.com",
            "email": "paurakh011@gmail.com",
            "connected": "1"
        })

        # When
        response = self.app.post('/teachers', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['teacherId']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        db.drop_all()
TeacherTest()