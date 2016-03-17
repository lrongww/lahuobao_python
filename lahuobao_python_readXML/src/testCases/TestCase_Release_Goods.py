# -*- coding: utf-8 -*- 
'''
Created on 2016年2月18日

@author: Administrator
'''
import unittest
import time


from commonFunction.WebDriverHelp import WebDriverHelp
from commonFunction.QT_Operations import QT_Operations
from commonFunction.DataOperations import DataOperations
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
        dataoper = DataOperations("TestCase_Release_Goods.xml")
        #登录
        QT_Operations().login(dataoper.readxml("login", "username"),dataoper.readxml("login", "password"))
        #统计发布货源前我的发布里面的记录数
        count_before = QT_Operations().release_count()
        print count_before
        #货主发布货源
        QT_Operations().release_goods(dataoper.readxml("release", "weight"),
                                       dataoper.readxml("release", "volume"), 
                                       "一口价", dataoper.readxml("release", "price"), 
                                       dataoper.readxml("release", "goodsvalue"))
        
        #统计发布货源后的记录数
        count_after = QT_Operations().release_count()
        print count_after
        assert count_after==count_before+1
        print count_after==count_before+1
    
    def testrelease_Quotedgoods(self):
        dataoper = DataOperations("TestCase_Release_Goods.xml")
        #登录
        QT_Operations().login(dataoper.readxml("login", "username"),dataoper.readxml("login", "password"))
        count_before = QT_Operations().release_count()
        print count_before
        #货主发布货源
        QT_Operations().release_goods(dataoper.readxml("release", "weight"),
                                       dataoper.readxml("release", "volume"), 
                                       "参考价", dataoper.readxml("release", "price"), 
                                       dataoper.readxml("release", "goodsvalue"))
        
        count_after = QT_Operations().release_count()
        print count_after
        assert count_after==count_before+1
        print count_after==count_before+1
    
    
    




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
