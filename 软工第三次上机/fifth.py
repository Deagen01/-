#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.dom.minidom

class Find():

    def __init__(self,path):
        #打开xml
        self.domTree=xml.dom.minidom.parse(path)
        #得到xml的根节点
        self.root=self.domTree.documentElement

        self.itemList=self.root.getElementsByTagName("item")
        self.wordList=self.root.getElementsByTagName("word")

        self.num=int(self.root.getElementsByTagName("num")[0].firstChild.data)

    def Output(self,i):
        # print(item.firstChild.data)
        print(self.itemList[i].getElementsByTagName("word")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("trans")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("phonetic")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("examples")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("examples_trans")[0].firstChild.data)
    
    def outPutLast(self):
        i=self.num-1
        # print(item.firstChild.data)
        print(self.itemList[i].getElementsByTagName("word")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("trans")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("phonetic")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("examples")[0].firstChild.data)
        print(self.itemList[i].getElementsByTagName("examples_trans")[0].firstChild.data)


    # def readXML(self):
    #     itemList=self.root.getElementsByTagName("item")
    #     wordList=self.root.getElementsByTagName("word")
    #     for item in itemList:
    #         Output(item)

    # def getNum(self):
    #     return self.root.getElementsByTagName("num")[0].firstChild.data

    def findWord(self,input_word):
        i=0
        for word in self.wordList:
            if(input_word==word.firstChild.data):
                break
            i=i+1
        if(i<self.num):
            return i
        else:
            print("fail to find "+input_word)
            return -1
   
