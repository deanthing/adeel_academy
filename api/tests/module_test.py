import unittest
import json
from main import app, db



class ModuleTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.create_all()

    def test(self):
        # Given
        payload = json.dumps({
            "name": "dean@gmail.com",
            "description": "asdf asdf asdf",
            "courseId": "1"
        })

        # When
        response = self.app.post('/module', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['moduleId']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        db.drop_all()
ModuleTest()