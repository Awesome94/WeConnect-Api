import flask
import json
import flask_jwt_extended
import unittest

from app import create_app
from app.v1 import models, users

class WeConnectViews(unittest.TestCase):
    """Tests the enpoints contains in views.py"""

    def setUp(self):
        self.weconnect_test = app.test_client(self)
        models.WeConnect.user_db = []
        models.WeConnect.business_db = []

    def tearDown(self):
        models.WeConnect.user_db = []

    def test_register_user(self):
        response = self.weconnect_test.post(
            '/api/v1/auth/register',
            content_type='application/json',
            data=json.dumps(
                dict(
                    first_name='Harry',
                    last_name='Potter',
                    email='harry@aol.com',
                    password='dumbledore')))
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        self.weconnect_test.post(
            '/api/v1/auth/register',
            content_type='application/json',
            data=json.dumps(
                dict(
                    first_name='Harry',
                    last_name='Potter',
                    email='harry@aol.com',
                    password='dumbledore')))
        response = self.weconnect_test.post(
            '/api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(
                dict(
                    email='harry@aol.com',
                    password='dumbledore')))
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        self.weconnect_test.post(
            '/api/v1/auth/register',
            content_type='application/json',
            data=json.dumps(
                dict(
                    first_name='Harry',
                    last_name='Potter',
                    email='harry@aol.com',
                    password='dumbledore')))
        login = self.weconnect_test.post(
            '/api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(
                dict(
                    email='harry@aol.com',
                    password='dumbledore')))
        resp = json.loads(login.data.decode())
        access_token = resp['access_token']
        response = self.weconnect_test.post(
            '/api/v1/auth/reset-password',
            content_type='application/json',
            data=json.dumps(
                dict(
                    email='harry@aol.com',
                    password='dumbledore',
                    new_password='severus snape')),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertEqual(response.status_code, 200)