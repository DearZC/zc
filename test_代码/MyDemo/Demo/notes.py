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


        #  保存截图
#     driver.get_screenshot_as_file('D:/zi.jpg')


        #  全部文字
# 	  java：driver.findElement(By.xpath("//*[text()=’退出’]");
# 	  python：driver.find_element_by_xpath("//*[text()='花呗套现']").click()
		#  部分文字
# 	  java：driver.findElement(By.xpath("//a[contains(text(), ’退出’)]");
# 	  python：driver.find_element_by_xpath("//*[contains(text(),'花呗')]").click()
