import unittest
import requests
import json


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def test_001_test(self):
        a = requests.get(url = 'http://192.168.1.216:1000/api/FriendshipLink')
        code = json.loads(a.text)
        print(code)
        self.assertEqual(a.status_code, 200)




if __name__ == '__main__':
    unittest.main()
