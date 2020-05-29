#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
# from first import openXML
from bs4 import BeautifulSoup
def openXML():
    path="second.xml"
    htmlfile=open(path,'r',encoding='utf-8')
    handle=htmlfile.read()
    s=BeautifulSoup(handle,'xml')
    return s

def test(soup):
    tag=soup.item
    print("test tag")
    print(tag)
    
    new_tag=soup.new_tag("test",id='0')
    tag.append(new_tag)
    #print("add new tag")
    #print(tag)
    new_tag.string="hello everyone"
    print("add text")
    print(tag)

    return
if ( __name__ == "__main__"):
    try:
        s=openXML()
        test(s)
        # print(s)
    except Exception:
        print("fail to open")

