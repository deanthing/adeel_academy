import unittest
import json
from ..main import app, db



class AnnouncmentTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.create_all()

    def test(self):
        # Given
        payload = json.dumps({
            "courseId": "1",
            "name": "asdf",
            "description": "asdf",
            "timeStamp": "1045",
        })

        # When
        response = self.app.post('/announcements', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['announcementId']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        db.drop_all()
AnnouncmentTest()