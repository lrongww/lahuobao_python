# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
import unittest
import time


from commonFunction.WebDriverHelp import WebDriverHelp
from commonFunction.QT_Operations import QT_Operations
from commonFunction.DataOperations import DataOperations
import sys 
sys.path.append("\commonFunction")


class testcases_login(unittest.TestCase):


    def setUp(self):
        #打开浏览器并打开拉货宝首页
        WebDriverHelp("firefox").geturl("http://v2.lahuobao.net")
        time.sleep(2)


    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器


    def testlogin(self):
        dataoper = DataOperations("TestCase_QT_Login.xml")
        #登录
        QT_Operations().login(dataoper.readxml("login", "username"),dataoper.readxml("login", "password"))
        #验证
        self.assertEqual(WebDriverHelp().get_text("id", "nowrap"), "lrong")
         #退出
        QT_Operations().logout()
        #验证
        self.assertEqual(WebDriverHelp().get_text("xpath", "/html/body/div[1]/div[2]/div/div/ul/li[1]/a"),"登录")  
    #def testlogout(self):
         
        #assert WebDriverHelp().get_text("xpath", "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")=="登录"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    '''
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(testcases_login("testlogin"))
    suite.addTest(testcases_login("testlogout"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''