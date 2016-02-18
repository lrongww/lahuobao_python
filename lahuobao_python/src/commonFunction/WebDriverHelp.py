# -*- coding: utf-8 -*- 
'''
Created on 2016年2月17日

@author: Administrator
'''
#对webdriver的再次封装
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class WebDriverHelp(object):
    '''
    本类主要完成页面的基本操作、如打开指定的URL，对页面上的元素进行操作等
    '''
    def __init__(self,atype="chorme"):
        global DRIVER
        if(atype=="firefox"):
            DRIVER = webdriver.Firefox()
            DRIVER.maximize_window()
        self.DRIVER=DRIVER
    def geturl(self,url):
        self.DRIVER.get(url)
    def teardown(self):
        #关闭浏览器
        self.DRIVER.quit()
        
    #点击
    def click_item(self,type,location):
        driver = self.DRIVER
        if type=="xpath":
            elem = driver.find_element_by_xpath(location)
        if type=="id":
            elem = driver.find_element_by_id(location)
        if type=="name":
            elem = driver.find_element_by_name(location)
        if type=="class":
            elem = driver.find_element_by_class_name(location)
        if type=="link":
            elem = driver.find_element_by_link_text(location) 
        if type=="css":
            elem = driver.find_element_by_css_selector(location)
        return elem.click()
    
    #获取text值
    def get_text(self,type,location):
        driver = self.DRIVER
        if type=="xpath":
            elem = driver.find_element_by_xpath(location)
        if type=="id":
            elem = driver.find_element_by_id(location)
        if type=="name":
            elem = driver.find_element_by_name(location)
        if type=="class":
            elem = driver.find_element_by_class_name(location)
        if type=="link":
            elem = driver.find_element_by_link_text(location) 
        if type=="css":
            elem = driver.find_element_by_css_selector(location)
        return elem.text
    
    #清除值
    def clear_value(self,type,location):
        driver = self.DRIVER
        if type=="xpath":
            elem = driver.find_element_by_xpath(location)
        if type=="id":
            elem = driver.find_element_by_id(location)
        if type=="name":
            elem = driver.find_element_by_name(location)
        if type=="class":
            elem = driver.find_element_by_class_name(location)
        if type=="link":
            elem = driver.find_element_by_link_text(location) 
        if type=="css":
            elem = driver.find_element_by_css_selector(location)
        return elem.clear()
    
    #输入值
    def input_value(self,type,location,value):
        driver = self.DRIVER
        if type=="xpath":
            elem = driver.find_element_by_xpath(location)
        if type=="id":
            elem = driver.find_element_by_id(location)
        if type=="name":
            elem = driver.find_element_by_name(location)
        if type=="class":
            elem = driver.find_element_by_class_name(location)
        if type=="link":
            elem = driver.find_element_by_link_text(location) 
        if type=="css":
            elem = driver.find_element_by_css_selector(location)
        return elem.send_keys(value)
        
    def house_hover(self,type,location):
        driver = self.DRIVER
        #建立动作链
        chain = ActionChains(driver)
        #定位元素
        if type=="xpath":
            elem = driver.find_element_by_xpath(location)
        if type=="id":
            elem = driver.find_element_by_id(location)
        if type=="name":
            elem = driver.find_element_by_name(location)
        if type=="class":
            elem = driver.find_element_by_class_name(location)
        if type=="link":
            elem = driver.find_element_by_link_text(location) 
        if type=="css":
            elem = driver.find_element_by_css_selector(location)
        #执行
        chain.move_to_element(elem).perform()
        
        
        
        
