# -*- coding: utf-8 -*- 
'''
Created on 2016年2月18日

@author: Administrator
'''
import unittest
import time


from commonFunction.WebDriverHelp import WebDriverHelp
from commonFunction.QT_Operations import QT_Operations
import sys 
sys.path.append("\commonFunction")

class testcases_release_goods(unittest.TestCase):


    def setUp(self):
        #打开浏览器并打开拉货宝首页
        WebDriverHelp("firefox").geturl("http://v2.lahuobao.net")
        time.sleep(2)


    def tearDown(self):
        WebDriverHelp().teardown()#关闭浏览器


    def testrelease_Fixedgoods(self):
        #登录
        QT_Operations().login("lrong", "123456")
        count_before = QT_Operations().release_count()
        print count_before
        #货主发布货源
        QT_Operations().release_goods("20", "200", "一口价", "3", "70000")
        
        count_after = QT_Operations().release_count()
        print count_after
        assert count_after==count_before+1
        print count_after==count_before+1

    def testrelease_Quotedgoods(self):
        #登录
        QT_Operations().login("lrong", "123456")
        count_before = QT_Operations().release_count()
        print count_before
        #货主发布货源
        QT_Operations().release_goods("30", "200", "参考价", "3", "70000")
        
        count_after = QT_Operations().release_count()
        print count_after
        assert count_after==count_before+1
        print count_after==count_before+1


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()