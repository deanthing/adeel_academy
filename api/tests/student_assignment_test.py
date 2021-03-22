import unittest
import json
from main import app, db



class StudentAssignmentTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.create_all()

    def test(self):
        # Given
        payload = json.dumps({
            "name": "dean@gmail.com",
            "description": "yup",
            "dueDate": "12378",
            "grade": "91.5",
            "turnedIn": "1"
        })

        # When
        response = self.app.post('/studentAssignments', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['assignmentId']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        db.drop_all()
StudentAssignmentTest()