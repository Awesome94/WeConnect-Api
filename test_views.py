import bcrypt, flask, json, flask_jwt_extended, unittest

from app import app, app_class, views

class WeConnectViews(unittest.TestCase):
    """Tests the enpoints contains in views.py"""
    def setUp(self):
        self.weconnect_test = app.test_client(self)
        app_class.WeConnect.user_db = []
        app_class.WeConnect.business_db = []

    def tearDown(self):
        app_class.WeConnect.user_db = []
        app_class.WeConnect.business_db = []

    def test_register_user(self):
        response = self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
                                           data=json.dumps(dict(first_name='Harry', last_name='Potter',
                                                               email='harry@aol.com', password='dumbledore')))
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
                                 data=json.dumps(dict(first_name='Harry', last_name='Potter',
                                                      email='harry@aol.com', password='dumbledore')))
        response = self.weconnect_test.post('/api/v1/auth/login', content_type='application/json',
                                           data=json.dumps(dict(email='harry@aol.com', password='dumbledore')))
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
                                 data=json.dumps(dict(first_name='Harry', last_name='Potter',
                                                      email='harry@aol.com', password='dumbledore')))
        login = self.weconnect_test.post('/api/v1/auth/login', content_type='application/json',
                                           data=json.dumps(dict(email='harry@aol.com', password='dumbledore')))
        resp = json.loads(login.data.decode())
        access_token = resp['access_token']
        response = self.weconnect_test.post('/api/v1/auth/reset-password', content_type='application/json',
                                           data=json.dumps(dict(email='harry@aol.com', password='dumbledore',
                                                               new_password='severus snape')),
                                           headers={'Authorization': 'Bearer %s' % access_token})
        self.assertEqual(response.status_code, 200)

    def test_register_business(self):
        self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
                                 data=json.dumps(dict(first_name='Harry', last_name='Potter',
                                                      email='harry@aol.com', password='dumbledore')))
        login = self.weconnect_test.post('/api/v1/auth/login', content_type='application/json',
                                           data=json.dumps(dict(email='harry@aol.com', password='dumbledore')))
        resp = json.loads(login.data.decode())
        access_token = resp['access_token']
        response = self.weconnect_test.post('/api/v1/businesses', content_type='application/json',
                            data=json.dumps(dict(name='Mortal Kombat', location='Earth', category='something',
                                            description='something', review=[])),
                                            headers={'Authorization': 'Bearer %s' % access_token})
        self.assertIn(b'Mortal Kombat', response.data)
        self.assertIn(b'Earth', response.data)
        self.assertIn(b'something', response.data)
        self.assertIn(b'user_id', response.data)
        self.assertEqual(response.status_code, 201)

    def test_update_business(self):
        self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
                                 data=json.dumps(dict(first_name='Harry', last_name='Potter',
                                                      email='harry@aol.com', password='dumbledore')))
        login = self.weconnect_test.post('/api/v1/auth/login', content_type='application/json',
                                         data=json.dumps(dict(email='harry@aol.com', password='dumbledore')))
        resp = json.loads(login.data.decode())
        access_token = resp['access_token']
        business = self.weconnect_test.post('/api/v1/businesses', content_type='application/json',
                                        data=json.dumps(dict(name='Mortal Kombat', location='Earth', category='something',
                                                        description='something', review=[])),
                                                        headers={'Authorization': 'Bearer %s' % access_token})
        biz_id = json.loads(business.get_data())['business']['business_id']
        response = self.weconnect_test.put('/api/v1/businesses/'+str(biz_id), content_type='application/json',
                                           data=json.dumps(dict(name='Mortal Kombat1', location='something_new',
                                                                category='something_new', description='something_new')),
                                           headers={'Authorization': 'Bearer %s' % access_token})
        self.assertIn(b'Mortal Kombat1', response.data)
        self.assertIn(b'something_new', response.data)
        self.assertIn(b'user_id', response.data)
        self.assertTrue(response.status_code, 201)

    # def test_get_business(self):
    #     self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
    #                              data=json.dumps(dict(first_name='Harry', last_name='Potter',
    #                                                   email='harry@aol.com', password='dumbledore')))
    #     login = self.weconnect_test.post('/api/v1/auth/login', content_type='application/json',
    #                                        data=json.dumps(dict(email='harry@aol.com', password='dumbledore')))
    #     resp = json.loads(login.data.decode())
    #     access_token = resp['access_token']
    #     business = self.weconnect_test.post('/api/v1/businesses', content_type='application/json',
    #                                     data=json.dumps(dict(name='Mortal Kombat', location='Earth', category='something',
    #                                                     description='something', review=[])),
    #                                                     headers={'Authorization': 'Bearer %s' % access_token})
    #     biz_id = json.loads(business.get_data())['business']['id']
    #     response = self.weconnect_test.get('/api/v1/businesses/'+str(biz_id), content_type='application/json',
    #                                        headers={'Authorization': 'Bearer %s' % access_token})
    #     self.assertEqual(response.status_code, 200)

    # def test_get_businesses(self):
    #     self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
    #                              data=json.dumps(dict(first_name='Harry', last_name='Potter',
    #                                                   email='harry@aol.com', password='dumbledore')))
    #     login = self.weconnect_test.post('/api/v1/auth/login', content_type='application/json',
    #                                        data=json.dumps(dict(email='harry@aol.com', password='dumbledore')))
    #     resp = json.loads(login.data.decode())
    #     access_token = resp['access_token']
    #     self.weconnect_test.post('/api/v1/businesses', content_type='application/json',
    #                         data=json.dumps(dict(name='Mortal Kombat', location='Earth', category='something',
    #                                         description='something', review=[])),
    #                                         headers={'Authorization': 'Bearer %s' % access_token})
    #     response = self.weconnect_test.get('/api/v1/businesses', content_type='application/json',
    #                                        headers={'Authorization': 'Bearer %s' % access_token})
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_business(self):
    #     self.weconnect_test.post('/api/v1/auth/register', content_type='application/json',
    #                              data=json.dumps(dict(first_name='Harry', last_name='Potter',
    #                                                   email='harry@aol.com', password='dumbledore')))
    #     login = self.weconnect_test.post('/api/v1/auth/login', content_type='application/json',
    #                                        data=json.dumps(dict(email='harry@aol.com', password='dumbledore')))
    #     resp = json.loads(login.data.decode())
    #     access_token = resp['access_token']
    #     business = self.weconnect_test.post('/api/v1/businesses', content_type='application/json',
    #                         data=json.dumps(dict(name='Mortal Kombat',
    #                                         location='Earth', category='something',
    #                                         description='something', review=[])),
    #                                         headers={'Authorization': 'Bearer %s' % access_token})
    #     biz_id = json.loads(business.get_data())['business']['id']
    #     response = self.weconnect_test.delete('/api/v1/businesses/'+str(biz_id),
    #                                           headers={'Authorization': 'Bearer %s' % access_token})
    #     self.assertTrue(response.status_code, 200)
    #     result = self.weconnect_test.get('/api/v1/businesses')
    #     self.assertEqual(0, len(json.loads(result.data.decode())['business']))

    # def test_get_reviews(self):
    #     resp = self.weconnect_test.post('/api/v1/businesses', content_type='application/json',
    #                         data=json.dumps(dict(name='Mortal Kombat',
    #                                         location='Earth', category='something',
    #                                         description='something',
    #                                         review=[])))
    #     biz_id = json.loads(resp.data.decode())['business']['id']
    #     response = self.weconnect_test.post('/api/v1/businesses/'+str(biz_id)+'/reviews',
    #                                         content_type='application/json', data=json.dumps(dict(review="Beautiful")))
    #     self.assertTrue(response.status_code, 200)
    #     response = self.weconnect_test.get('/api/v1/businesses/'+str(biz_id)+'/reviews')
    #     self.assertTrue(response.status_code, 200)
    #     response = self.weconnect_test.delete('/api/v1/businesses/'+str(biz_id))

    # def test_add_review(self):
    #     resp = self.weconnect_test.post('/api/v1/businesses', content_type='application/json',
    #                         data=json.dumps(dict(name='Mortal Kombat',
    #                                         location='Earth', category='something',
    #                                         description='something',
    #                                         review=[])))
    #     biz_id = json.loads(resp.data.decode())['business']['id']
    #     response = self.weconnect_test.post('/api/v1/businesses/'+str(biz_id)+'/reviews',
    #                                         content_type='application/json', data=json.dumps(dict(review="Beautiful")))
    #     self.assertTrue(response.status_code, 200)
    #     response = self.weconnect_test.get('/api/v1/businesses/'+str(biz_id)+'/reviews')
    #     self.assertTrue(response.status_code, 200)
    #     response = self.weconnect_test.delete('/api/v1/businesses/'+str(biz_id))


if __name__ == '__main__':
    unittest.main()