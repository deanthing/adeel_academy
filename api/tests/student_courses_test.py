import unittest
import json
from ..main import app, db



class StudentCourses(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.create_all()

    def test(self):
        # Given
        payload = json.dumps({
            "courseId": "1",
            "studentId": "1",
        })

        # When
        response = self.app.post('/studentcourses', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['studentCourseId']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        db.drop_all()

StudentCourses()