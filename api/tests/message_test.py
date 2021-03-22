import unittest
import json
from ..main import app, db



class Message(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.create_all()

    def test(self):
        # Given
        payload = json.dumps({
            "chatId": "1",
            "userId": "1",
            "message": "my message",
            "timeStamp": "1839",
        })

        # When
        response = self.app.post('/messages', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(int, type(response.json['messageId']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        db.drop_all()
Message()