# -*- coding: utf-8 -*- 
'''
Created on 2016年3月15日

@author: Administrator
'''
import unittest
import sys
import os


from TestCase_QT_Login import testcases_login
from TestCase_Release_Goods import testcases_release_goods
from TestCase_Driver_Offer import Testcases_driver_offer

class Testsuite_all():


    def test(self):
        if __name__=="__main__":
            suite = unittest.TestSuite()
            suite.addTest(testcases_login('testlogin'))
            suite.addTest(testcases_release_goods ('testrelease_Fixedgoods'))
            suite.addTest(testcases_release_goods ('testrelease_Quotedgoods'))
            suite.addTest(Testcases_driver_offer ('testDriverApplyToDeal'))
            # 运行测试用例集
            runner = unittest.TextTestRunner()
            runner.run(suite)
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    Testsuite_all().test()