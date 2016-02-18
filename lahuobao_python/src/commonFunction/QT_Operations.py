# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
#公共功能模块的封装
import time
from WebDriverHelp import WebDriverHelp

class QT_Operations():  
    #登录
    def login(self,username,passwd):
        WebDriverHelp().click_item("xpath", "/html/body/div[1]/div[2]/div/div/ul/li[1]/a")
        time.sleep(2)
        WebDriverHelp().clear_value("name", "userName")
        WebDriverHelp().input_value("name","userName",username)
        WebDriverHelp().clear_value("name", "password")
        WebDriverHelp().input_value("name","password",passwd)
        WebDriverHelp().click_item("xpath", "/html/body/div/div/div/form/div[1]/div[3]/input")
        time.sleep(2)
    
    def logout(self):
        WebDriverHelp().house_hover("id", "nowrap")  
        #点击退出菜单
        WebDriverHelp().click_item("link", "退出")
        time.sleep(2)