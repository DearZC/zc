import requests
import json
import unittest

b = requests.get(url="https://news-static.a8sport.com/right/news/news_html")

print(b.status_code)
print(b.text)


c = requests.post(url="http://dspdev.ssptest.gionee.com/check/login",
                  params={"username":"gionee_test","password":"gionee_test","image_verify_code":"2017"})

print(c.status_code)
print(c.text)

class jiekou(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_001(self):
        d = requests.get(url="http://a8.tvesou.com/v3/game/list?",
                  params={"page":"0","pageSize":"2","type":"2","status":"fin"})
        code = json.loads(d.text)
        print(d.status_code)
        print(code)
        self.assertEqual(d.get_status_code(), 200)
        self.assertEqual(d.get_code(), 1)

if __name__ == '__main__' :
    unittest.main()
