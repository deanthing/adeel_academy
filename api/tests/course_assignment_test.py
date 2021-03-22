import unittest
import json
from main import app, db



class CourseAssignmentTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.create_all()

    def test(self):
        # Given
        payload = json.dumps({
            "courseId": "1",
            "moduleId": "1",
            "name": "class",
            "descriptiopn": "1232",
            "dueDate": "1760",
        })

        # When
        response = self.app.post('/courseAssignments', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['courseAssignmentId']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        db.drop_all()

CourseAssignmentTest()