# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
import unittest
import time


from commonFunction.WebDriverHelp import WebDriverHelp
from commonFunction.QT_Operations import QT_Operations
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
        #登录
        QT_Operations().login("lrong", "123456")
        #验证
        self.assertEqual(WebDriverHelp().get_text("id", "nowrap"), "lrong")
        #退出
        QT_Operations().logout()
        #验证
        self.assertEqual(WebDriverHelp().get_text("xpath", "/html/body/div[1]/div[2]/div/div/ul/li[1]/a"),"登录")  
        #assert WebDriverHelp().get_text("xpath", "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")=="登录"
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()