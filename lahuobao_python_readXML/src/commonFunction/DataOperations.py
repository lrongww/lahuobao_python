# -*- coding: utf-8 -*- 
'''
Created on 2016年2月19日

@author: Administrator
'''
from xml.dom import minidom


global DOC,CONN
class DataOperations(object):
    #数据读取相关操作
    def __init__(self,filename):
        #初始化xml文档
        global DOC,CONN
        DOC = minidom.parse("../testData/"+filename)
    def readxml(self,firstname,secondname):
        '''
        firstname为起始节点的名称
        num为取起始节点相同的第num个节点
        secondname为起始节点下的二级节点名称
        '''
        root = DOC.documentElement
        message = root.getElementsByTagName(firstname)[0]
        print message.getElementsByTagName(secondname)[0].childNodes[0].nodeValue
        return message.getElementsByTagName(secondname)[0].childNodes[0].nodeValue
        
    def readxml_attribute(self,firstname,secondname,attributeName):
        root = DOC.documentElement
        message = root.getElementsByTagName(firstname)[0]
        return message.getElementByTagaName(secondname)[0].getAttribute(attributeName)


        