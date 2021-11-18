import unittest
import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_message(self):
        response = self.app.get('/')
        arg1 = 'The hostname of the container is'
        self.assertIn(arg1 , response.data, msg=None)
        
if __name__=='__main__':
    unittest.main()
