#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xml.dom.minidom


def Output(item):
   # print(item.firstChild.data)
   print(item.getElementsByTagName("word")[0].firstChild.data)
   print(item.getElementsByTagName("trans")[0].firstChild.data)
   print(item.getElementsByTagName("phonetic")[0].firstChild.data)


def openXML():
   #打开xml
   dom=xml.dom.minidom.parse("second.xml")
   #得到xml的根节点
   root=dom.documentElement
   return root



def readXML(root):
   itemList=root.getElementsByTagName("item")
   wordList=root.getElementsByTagName("word")
   for item in itemList:
      Output(item)

def getItemList(root):
   return root.getElementsByTagName("item")

def getWordList(root):
   return root.getElementsByTagName("word")
def getNum(root):
   return root.getElementsByTagName("num")[0].firstChild.data

def findWord(input,root):
   itemList=getItemList(root)
   wordList=getWordList(root)
   num=int(getNum(root))
   i=0
   for word in wordList:
      if(input==word.firstChild.data):
         break
      i=i+1
   if(i<num):
      Output(itemList[i])
   else:
      print("fail to find "+input)
   
         


if ( __name__ == "__main__"):
   while(1):
      print("**************************************")
      word=input("请输入一个单词,退出请按q\n")
      if(word=='q'):
         break
      root=openXML()
      # readXML(root)
      findWord(word,root)
      


   
