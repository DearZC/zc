from Hdl.backstage.Home import home
import unittest
import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(home))
    html = "D://test.html"
    f = open(html, 'wb')
    run = HTMLTestRunner.HTMLTestRunner(f, title='用例标题', description='用例描述')
    run.run(suite)