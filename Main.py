# coding=utf-8


from A8_regress.Login import login
from A8_regress.Update import version
import unittest
import HTMLTestRunner


if __name__ == '__main__':       
        #  添加类里所有的用例
#     test_suite.addTests(unittest.makeSuite(open))
        #  添加类里想要执行的用例
#     test_suite.addTest(open('test_001_my'))
        #  执行测试用例
#     test_run = unittest.TextTestRunner()
#     test_run.run(test_suite) 
        #  导出测试结果并运行测试
#     html = "D:\\test.html"
#     f = open(html,'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(f, title='unittest用例标题', description='这是用例描述')
#     runner.run(test_suite)
   
    test_suite = unittest.TestSuite()
#     test_suite.addTests(unittest.makeSuite(login))
    test_suite.addTest(version('test_001_version'))
    test_run = unittest.TextTestRunner()
    test_run.run(test_suite)
    
#     html = "D:\\test.html"
#     f = open(html, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(f, title='A8测试环境回归', description='回归测试用例')
#     runner.run(test_suite)
            
