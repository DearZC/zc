import unittest
from test_代码.HDL.Interface.interface import MyTestCase
import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(MyTestCase))
    report = 'D:\\testReport.html'
    a = open(report, 'wb')
    run = HTMLTestRunner.HTMLTestRunner(a)
    run.run(suite)




