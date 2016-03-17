# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
#具体公共功能模块的封装
import time
from WebDriverHelp import WebDriverHelp


class QT_Operations():  
    #车货主切换
    def switch_role(self,role):
        
        try:
            WebDriverHelp().get_text("id", "navTagReleaseCargo")
            a = True
        except:
            a = False
           
        if(role =="车主"):
            if(a):
                #鼠标悬停在用户名账户上
                WebDriverHelp().house_hover("id", "nowrap")
                WebDriverHelp().click_item("xpath","/html/body/div[1]/div[2]/div/div/form/dl/dd[8]/a")
        if(role == "货主"):
            if(a==0):
                #鼠标悬停在用户名账户上
                WebDriverHelp().house_hover("id", "nowrap")
                WebDriverHelp().click_item("xpath","/html/body/div[1]/div[2]/div/div/form/dl/dd[10]/a ")
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
        WebDriverHelp().selectplace("xpath","//*[@value='成都市']", "//*[@id='510108']")
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
        
        WebDriverHelp().pulldown_select("id", "sl-payment-method", "//select[@id='sl-payment-method']/option[@value='3']")
        
        WebDriverHelp().click_item("id", "ckb_manager_service")
        WebDriverHelp().click_item("id", "ckb_tran_management")
        WebDriverHelp().click_item("id", "ckb_invoice")
        WebDriverHelp().click_item("id", "ckb_logistics_insure")
        WebDriverHelp().input_value("id", "logicsticsCargoValueBox", goodsvalue)
        WebDriverHelp().click_item("id", "submitCargoInfo")
        time.sleep(5)
    def driver_offer(self):
        WebDriverHelp().click_item("id", "navTagHome")
        WebDriverHelp().click_item("css", "input.u-btn.u-btn-sm.btn_more")
        '''
                            暂时没有考虑首页翻页的问题
                            未考虑已报车辆
        '''
        
        WebDriverHelp().click_item("xpath", "/html/body/div[2]/div[2]/table/tbody/tr[1]")
        divs = WebDriverHelp().find_elements("xpath", "/html/body/div[2]/div[1]/div[2]/div[4]/div/input")
        for div in divs:
            style = div.get_attribute("value")
            print style
        WebDriverHelp().click_item("xpath", "/html/body/div[2]/div[1]/div[2]/div[4]/div/input")
        #判断为报价还是是申请立即成交 
        if(style=="申请立即成交"):
            WebDriverHelp().click_item("id", "lyBuyNowbtnok")
        elif(style=="报价"):
            WebDriverHelp().input_value("xpath", "/html/body/div[4]/form/table/tbody/tr/td/div/div[2]/div[1]/div/input", "5")
            WebDriverHelp().click_item("id", "lyofferpricebtnok")   
        
     #判断我的发布的列表数
    def release_count(self):
        WebDriverHelp().click_item("id", "navTagQuoteMag")
        lists = WebDriverHelp().find_elements("xpath", "//div[@id='preOnLine']/table/tbody/tr")
        count = 0
        for lis in lists:
            count+= 1
        for i in range(1,10):
            if count==10*i:
                WebDriverHelp().click_item("xpath", "//div[@id='pagination']/a[4]")
                lists = WebDriverHelp().find_elements("xpath", "//div[@id='preOnLine']/table/tbody/tr")
                for lis in lists:
                    count = count + 1
        return count
    
                
 
    #判断我的报价列表数
    def offer_count(self):
        WebDriverHelp().click_item("id", "navTagMyQuote")
        lists = WebDriverHelp().find_elements("xpath", "//form[@id='fm_myQuotesForm']/table/tbody/tr")
        count = 0
        for lis in lists:
            count+= 1
        for i in range(1,10):
            if count==10*i:
                WebDriverHelp().click_item("xpath", "//div[@id='pagination']/a[4]")
                lists = WebDriverHelp().find_elements("xpath", "//form[@id='fm_myQuotesForm']/table/tbody/tr")
                for lis in lists:
                    count = count + 1
        return count
        
        
        
        
        
        
            
            
            
    
            
            
                
                    
        
    
        
    
            
            
                
            
            
        