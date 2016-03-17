# -*- coding: utf-8 -*- 
'''
Created on 2016年3月14日

@author: Administrator
'''
import unittest
import time
from commonFunction.WebDriverHelp import WebDriverHelp
from commonFunction.QT_Operations import QT_Operations


class Testcases_driver_offer(unittest.TestCase):


    def setUp(self):
        #打开浏览器并打开拉货宝首页
        WebDriverHelp("firefox").geturl("http://v2.lahuobao.net")
        time.sleep(2)


    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器


    def testDriverApplyToDeal(self):
        #登录
        QT_Operations().login("lrong","123456")
        QT_Operations().switch_role("车主")
        print QT_Operations().offer_count()
        QT_Operations().driver_offer()
        print QT_Operations().offer_count()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()