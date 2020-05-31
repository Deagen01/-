#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.dom.minidom

class LocalOper():

    def __init__(self,path):
        self.path=path
        #打开xml
        self.domTree=xml.dom.minidom.parse(path)
        #得到xml的根节点
        self.root=self.domTree.documentElement

        self.itemList=self.root.getElementsByTagName("item")
        self.wordList=self.root.getElementsByTagName("word")

        self.item=self.domTree.createElement("item")
        self.num=int(self.root.getElementsByTagName("num")[0].firstChild.data)

    def printWordMessage(self,i):
        # print(item.firstChild.data)
        print(self.itemList[i].getElementsByTagName("word")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("trans")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("phonetic")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("examples")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("examples_trans")[0].firstChild.data)
    # def getNumOfItem(self):
    #     i=0
    #     for word in self.wordList:
    #        i+=1
    #     return i 


    def getWordNum(self,input_word):
        i=0
        for word in self.wordList:
            if(input_word==word.firstChild.data):
                break
            i=i+1
        if(i<self.num):
            return i
        else:
            # print("fail to get Num ")
            return -1
   
    def addNodeCDATA(self,nodeName,CDATA):
        dom=self.domTree
        node=dom.createElement(nodeName)
        node_text=dom.createCDATASection(CDATA)
        node.appendChild(node_text)
        self.item.appendChild(node)

    def addNum(self):
        self.root.getElementsByTagName("num")[0].childNodes[0].data=self.num+1
   

    def addNode(self,name,text):
        dom=self.domTree
        # string="大家好我是测试君~"
        node=dom.createElement(name)
        node_text=dom.createTextNode(text)
        node.appendChild(node_text)
        self.item.appendChild(node)

    def rewrite(self):
        self.root.appendChild(self.item)
        with open(self.path,'w',encoding='utf-8') as f:
            self.domTree.writexml(f,addindent=' ',encoding='utf-8')
