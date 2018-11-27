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
        a = requests.get('http://192.168.1.216:1000/api/FriendshipLink')
        print('a的数据：%s' % a)
        self.assertEqual(a.status_code, 200)
        b = a.json()
        print('b的数据：%s' % b)
        assert b[0]["Name"] == '苹果维修点'
        assert b[1]["Name"] == '苹果维修站点'

    def test_002_test1(self):
        a = requests.post('https://gateway.open.umeng.com/openapi/param2/1/com.umeng.uapp/umeng.uapp.getTodayYesterdayData/5099339')
        self.assertEqual(a.status_code, 200)
        b = a.json()
        print(b)

if __name__ == '__main__':
    unittest.main()
