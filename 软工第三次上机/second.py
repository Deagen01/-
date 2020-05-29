#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

# 输出单词词义
def outPutTrans(soup):
    s = soup.find(class_='trans-container')('ul')[0]('li')
    for item in s:
        if item.text:
            print(item.text)
# 输出例句及其翻译
def outPutExamples(soup):
    exList=soup.find(class_="trans-container tab-content",id="bilingual")('ul')[0]('li')
    ex1=exList[0]('p')
    print("例句")
    print(ex1[0].get_text())
    print("翻译")
    print(ex1[1].get_text())
def outPutPhonetic(soup):
    s=soup.find(class_="phonetic")
    print("发音")
    print(s.get_text())
def output(soup):
    outPutTrans(soup)
    outPutPhonetic(soup)
    outPutExamples(soup)
# get word from Command line
word = input("Enter a word (enter 'q' to exit): ")

# main body
while word != 'q': # 'q' to exit
    try:
        # 利用GET获取输入单词的网页信息
        r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top'%word)
        # r=requests.get(url='https://www.collinsdictionary.com/zh/dictionary/english/%s'%word)
        # 利用BeautifulSoup将获取到的文本解析成HTML
        soup = BeautifulSoup(r.text, "lxml")
        # 获取字典的标签内容
        #测试
        # s2=soup.find(class_='trans-container')
        # print("trans-container:",s2)
        output(soup)
 
        # print(soup)
        print('='*40+'\n')
    except Exception:
        print("Sorry, there is a error!\n")
    finally:
        word = input( "Enter a word (enter 'q' to exit): ")
print("soup",soup)
