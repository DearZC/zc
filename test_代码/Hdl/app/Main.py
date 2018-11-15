import unittest
import  HTMLTestRunner
from test_代码.HDL.app.Home import home
import time


if __name__ == '__main__' :
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.makeSuite(home))
    # report = 'D:\\testReport.html'
    # a = open(report, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(a)
    # runner.run(suite)
    suite = unittest.TestSuite()
    suite.addTest(home('test_001_login'))
    time.sleep(2)
    suite.addTest(home('test_004_order'))
    run = unittest.TextTestRunner()
    run.run(suite)
