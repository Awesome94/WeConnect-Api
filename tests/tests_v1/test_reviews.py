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
        models.WeConnect.business_db = []

    def test_add_review(self):
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
        biz_id = json.loads(business.data.decode())['business']['business_id']
        review = self.weconnect_test.post(
            '/api/v1/businesses/' + str(biz_id) + '/reviews',
            content_type='application/json',
            data=json.dumps(
                dict(
                    review="Beautiful")),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertIn(b'review_id', review.data)
        self.assertTrue(review.status_code, 200)

    def test_get_reviews(self):
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
        biz_id = json.loads(business.data.decode())['business']['business_id']
        self.weconnect_test.post(
            '/api/v1/businesses/' + str(biz_id) + '/reviews',
            content_type='application/json',
            data=json.dumps(
                dict(
                    review="Beautiful")),
            headers={
                'Authorization': 'Bearer %s' % access_token})
        get_review = self.weconnect_test.get(
            '/api/v1/businesses/' + str(biz_id) + '/reviews',
            content_type='application/json',
            headers={
                'Authorization': 'Bearer %s' % access_token})
        self.assertTrue(get_review.status_code, 200)


if __name__ == '__main__':
    unittest.main()
