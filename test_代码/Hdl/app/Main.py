import unittest
import  HTMLTestRunner
from app.Home import home


if __name__ == '__main__' :
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.makeSuite(home))
    # report = 'D:\\testReport.html'
    # a = open(report, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(a)
    # runner.run(suite)
    suite = unittest.TestSuite()
    suite.addTest(home('test_004_order'))
    run = unittest.TextTestRunner()
    run.run(suite)
