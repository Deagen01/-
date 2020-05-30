#!/usr/bin/python
# -*- coding: utf-8 -*-
import xml.dom.minidom

class Storage:

   @staticmethod
   def Output(item):
      # print(item.firstChild.data)
      print(item.getElementsByTagName("word")[0].firstChild.data)
      print(item.getElementsByTagName("trans")[0].firstChild.data)
      print(item.getElementsByTagName("phonetic")[0].firstChild.data)


   # def openXML(self,path):
   #    #打开xml
   #    self.dom=xml.dom.minidom.parse(path)
   #    #得到xml的根节点
   #    root=self.dom.documentElement
   #    return root



   # def readXML(root):
   #    itemList=root.getElementsByTagName("item")
   #    wordList=root.getElementsByTagName("word")
   #    for item in itemList:
   #       Output(item)

   def getItemList(self):
      return self.root.getElementsByTagName("item")
   @staticmethod
   def addNum(root):
      root.getElementsByTagName("num")[0].firstChild.data=Storage.getNum(root)+1
   
   @staticmethod
   def getNum(root):
      return int(root.getElementsByTagName("num")[0].firstChild.data)

   # def findWord(self):
   #    itemList=getItemList(root)
   #    wordList=getWordList(root)
   #    num=int(getNum(root))
   #    i=0
   #    for word in wordList:
   #       if(input==word.firstChild.data):
   #          break
   #       i=i+1
   #    if(i<num):
   #       Output(itemList[i])
   #       return itemList[i]
   #    else:
   #       print("fail to find "+input)
      

   def addNode(self,item,nodeName,nodeText):
      node=self.dom.createElement(nodeName)
      node_text=self.dom.createElement(nodeText)
      node.appendChild(node_text)
      item.appendChild(node)
   @staticmethod
   def addNodeCDATA(dom,root,item,nodeName,CDATA):
      node=dom.createElement(nodeName)
      node_text=dom.createCDATASection(CDATA)
      node.appendChild(node_text)
      item.appendChild(node)
   def getDom(self):
      return self.dom
   def getRoot(self):
      return self.root
   # 增添一个单词
   @staticmethod
   def rewrite(dict):
      path="second.xml"
      domTree=xml.dom.minidom.parse(path)
      #得到xml的根节点
      root=domTree.documentElement
      #建立item节点
      item=domTree.createElement("item")
      #建立节点
      name_node=domTree.createElement("word")
      name_text_value=domTree.createTextNode(dict["word"])
      name_node.appendChild(name_text_value)  
      item.appendChild(name_node)

      
      Storage.addNodeCDATA(domTree,root,item,"trans",dict["trans"])
      Storage.addNodeCDATA(domTree,root,item,"phonetic",dict["phonetic"])
      Storage.addNodeCDATA(domTree,root,item,"examples",dict["examples"])

      name_node=domTree.createElement("tags")
      name_text_value=domTree.createTextNode("未分组")
      name_node.appendChild(name_text_value)  
      item.appendChild(name_node)

      name_node=domTree.createElement("progress")
      name_text_value=domTree.createTextNode("1")
      name_node.appendChild(name_text_value)  
      item.appendChild(name_node)

      #添加到根节点
      root.appendChild(item)
      Storage.addNum(root)
      with open('added_data.xml','w',encoding='utf-8') as f:
         domTree.writexml(f,addindent=' ',encoding='utf-8')
   # @staticmethod
   # def outPutAll():
   #    itemsList=self.root.getElementsByTagName("item")
   #    for i in range(getNum(self)):
   #       Output(itemsList[i])
   def __init__(self,word):
      self.word=word
      path="second.xml"
      self.dom=xml.dom.minidom.parse(path)
      #得到xml的根节点
      self.root=self.dom.documentElement
if ( __name__ == "__main__"):
   path="second.xml"
   path2="added_data.xml"
   word=input("请输入一个单词")

   #storage=Storage(word)
   dict={"word":"单词","trans":"词义","phonetic":"音标","examples":"例句","examples_trans":"例句翻译"}
   Storage.rewrite(dict)

   # outPutAll(root)
   

      


   