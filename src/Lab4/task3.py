import unittest
import task1

class RegistrationFormTests(unittest.TestCase):
    def setUp(self):
        self.app = task1.app.test_client()
        self.app.testing = True
        task1.app.config['WTF_CSRF_ENABLED'] = False

    def test_valid_email(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_email_format(self):
        response = self.app.post('/registration', data={
            'email': 'invalid-email',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.get_json()['errors'])

    def test_valid_phone(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone_length(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 12345,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('phone', response.get_json()['errors'])

    def test_valid_name(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_name_empty(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': '',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.get_json()['errors'])

    def test_valid_address(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_address_empty(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('address', response.get_json()['errors'])

    def test_valid_index(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_index_negative(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': -123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('index', response.get_json()['errors'])

    def test_invalid_index_empty(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': '',
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('index', response.get_json()['errors'])

    def test_valid_comment(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)

    def test_comment_not_required(self):
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'Test User',
            'address': '123 Test St',
            'index': 123456,
            'comment': ''
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()