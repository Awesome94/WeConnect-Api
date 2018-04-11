import flask
import json
import flask_jwt_extended
import unittest

from app import app
from app.v1 import models, users

class WeConnectViews(unittest.TestCase):
    """Tests the enpoints contains in views.py"""

    def setUp(self):
        self.weconnect_test = app.test_client(self)
        models.WeConnect.user_db = []
        models.WeConnect.business_db = []

    def tearDown(self):
        models.WeConnect.user_db = []
        models.WeConnect.business_db = []

    def test_register_business(self):
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
            '/api/v1/businesses',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Mortal Kombat',
                    location='Earth',
                    category='something',
                    description='something',
                    review=[])),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertIn(b'business_id', response.data)
        self.assertIn(b'user_id', response.data)
        self.assertEqual(response.status_code, 201)

    def test_update_business(self):
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
        business = self.weconnect_test.post(
            '/api/v1/businesses',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Mortal Kombat',
                    location='Earth',
                    category='something',
                    description='something',
                    review=[])),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        biz_id = json.loads(business.get_data())['business']['business_id']
        response = self.weconnect_test.put(
            '/api/v1/businesses/' + str(biz_id),
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Mortal Kombat1',
                    location='something new',
                    category='something new',
                    description='something new')),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertIn(b'Mortal Kombat1', response.data)
        self.assertIn(b'something new', response.data)
        self.assertIn(b'business_id', response.data)
        self.assertIn(b'user_id', response.data)
        self.assertTrue(response.status_code, 201)

    def test_get_business(self):
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
        business = self.weconnect_test.post(
            '/api/v1/businesses',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Mortal Kombat',
                    location='Earth',
                    category='something',
                    description='something',
                    review=[])),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        biz_id = json.loads(business.get_data())['business']['business_id']
        response = self.weconnect_test.get(
            '/api/v1/businesses/' + str(biz_id),
            content_type='application/json',
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertEqual(response.status_code, 200)

    def test_get_businesses(self):
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
        self.weconnect_test.post(
            '/api/v1/businesses',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Mortal Kombat',
                    location='Earth',
                    category='something',
                    description='something',
                    review=[])),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        response = self.weconnect_test.get(
            '/api/v1/businesses',
            content_type='application/json',
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertEqual(response.status_code, 200)

    def test_delete_business(self):
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
        business = self.weconnect_test.post(
            '/api/v1/businesses',
            content_type='application/json',
            data=json.dumps(
                dict(
                    name='Mortal Kombat',
                    location='Earth',
                    category='something',
                    description='something',
                    review=[])),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        biz_id = json.loads(business.get_data())['business']['business_id']
        response = self.weconnect_test.delete(
            '/api/v1/businesses/' + str(biz_id),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertTrue(response.status_code, 200)
        result = self.weconnect_test.get(
            '/api/v1/businesses',
            content_type='application/json',
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertEqual(
            0, len(
                json.loads(
                    result.data.decode())['businesses']))

if __name__ == '__main__':
    unittest.main()
