import unittest
import os
import json
from rest import create_app


class AppTestCase(unittest.TestCase):
    """This class represents the app test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_app_creation(self):
        """Test API can create a APP (GET request)"""
        name = 'pepe'
        res = self.client().get('/hello/{}'.format(name))
        jresponse = json.loads(res.data, encoding="utf-8")
        msg = 'Hello {}'.format(name)
        self.assertEqual(res.status_code, 200)
        self.assertIn(msg, jresponse['message'])

if __name__ == "__main__":
    unittest.main()
