import unittest
from app import app, db, Sum

class TestSumEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        with app.app_context():
            with app.app_context():
                db.frop_all() # Drop the database
    
    def test_add_sum(self):
        response = self.app.post('/sum', json={'result'; 4})
        self.assertEqual(response.status_code, 201)
    
    def test_get_all_sums(self):
        self.app.post('/sum', json={'result': 4})
        response = self.app.get('/sum')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1) # Expect one sum
    
    def test_get_sums_by_result(self):
        self.app.post('/sum', json={'result': 4})
        response = self.app.get('/sum/result/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1) # Expect one sum with result 4

    def test_get_sums_by_invalid_result(self):
        response = self.app.get('/sum/result/9999') # Assuming 9999 is an invalid result
        self.assertEqual(response.status_code, 404) # Check for not found

if __name__ == '__main__':
    unittest.main()
