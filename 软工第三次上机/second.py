#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

class GetNewWord:

    
    # 存储单词词义
    def storeTrans(self):
        s = self.soup.find(class_='trans-container')('ul')[0]('li')
        text=""
        for item in s:
            if item.text:
                text=text+"\n"+item.text
        self.dict["trans"]=text
    # 存储例句及其翻译
    def storeExamples(self):
        exList=self.soup.find(class_="trans-container tab-content",id="bilingual")('ul')[0]('li')
        ex1=exList[0]('p')
        self.dict["examples"]=ex1[0].get_text()
        self.dict["examples_trans"]=ex1[1].get_text()
    def storePhonetic(self):
        s=self.soup.find(class_="phonetic")
        self.dict["phonetic"]=s.get_text()
    def output(self):
        if(self.soup!=None):
            for i in self.dict.values():
                print(i)
    def isGetSoup(self):
        if self != None:
            return True
        else:
            return False
    def getDict(self):
        return self.dict
    def __init__(self,input_word):
        self.soup=None        
        self.dict={"word":"单词","trans":"词义","phonetic":"音标","examples":"例句","examples_trans":"例句翻译"}
        # get word from Command line
        try:
            # 利用GET获取输入单词的网页信息
            r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top'%input_word)
            # r=requests.get(url='https://www.collinsdictionary.com/zh/dictionary/english/%s'%word)
            # 利用BeautifulSoup将获取到的文本解析成HTML
            self.soup = BeautifulSoup(r.text, "lxml")
            #设定词典单词信息
            self.dict["word"]=input_word
            print('='*40+'\n')
        except Exception:
            print("Sorry, there is a error!\n")


