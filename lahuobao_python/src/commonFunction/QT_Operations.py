# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
#具体公共功能模块的封装
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
        
    def release_goods(self,weight,volume,atype,price,goodsvalue):
        WebDriverHelp().click_item("id", "navTagReleaseCargo")
        
        #目的地
        WebDriverHelp().click_item("id", "cargoTo")
        WebDriverHelp().selectplace("id","110100", "110115")
        WebDriverHelp().input_value("id", "weight", weight)
        WebDriverHelp().input_value("id", "volume", volume)
        if atype == "一口价":
            if WebDriverHelp().checked("id", "ckb_bidprice")==False:
                WebDriverHelp().click_item("id", "ckb_bidprice")
            if WebDriverHelp().checked("id", "ckb_quoteprice")==True:
                 WebDriverHelp().click_item("id", "ckb_quoteprice")
            WebDriverHelp().clear_value("id", "bidpricebox")
            WebDriverHelp().input_value("id", "bidpricebox", price)    
        elif atype == "参考价":
            if WebDriverHelp().checked("id", "ckb_bidprice")==True:
                WebDriverHelp().click_item("id", "ckb_bidprice")
            if WebDriverHelp().checked("id", "ckb_quoteprice")==False:
                 WebDriverHelp().click_item("id", "ckb_quoteprice")
            WebDriverHelp().clear_value("id", "referencePrice")
            WebDriverHelp().input_value("id", "referencePrice", price)
        
        WebDriverHelp().pulldown_select("id", "sl-payment-method", "//select[@id='sl-payment-method']/option[@value='6']")
        
        WebDriverHelp().click_item("id", "ckb_tran_management")
        WebDriverHelp().click_item("id", "ckb_invoice")
        WebDriverHelp().click_item("id", "ckb_logistics_insure")
        WebDriverHelp().input_value("id", "logicsticsCargoValueBox", goodsvalue)
        WebDriverHelp().click_item("id", "submitCargoInfo")
        time.sleep(5)
        #判断我的发布的列表数
    def release_count(self):
        WebDriverHelp().click_item("id", "navTagQuoteMag")
        lists = WebDriverHelp().find_elements("xpath", "//div[@id='preOnLine']/table/tbody/tr")
        count = 0
        for lis in lists:
            count+=1
        return count
    
        
    
            
            
                
            
            
        