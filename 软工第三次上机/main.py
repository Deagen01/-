#!/usr/bin/python
# -*- coding: utf-8 -*-
from MakeDict import makeDict
from LocalOperation import LocalOper


def storeToDict(myDict):
    try:
        myDict.storeTransToDict()
        myDict.storePhoneticToDict()
        myDict.storeExamplesToDict()
        return 0
    except Exception:
        print("sorry ,fail to find it ")
        return -1
def writeLocal(localOper,myDict):
    localOper.addNode("word",myDict["word"])
    localOper.addNodeCDATA("trans",myDict["trans"])
    localOper.addNodeCDATA("phonetic",myDict["phonetic"])
    localOper.addNodeCDATA("examples",myDict["examples"])
    localOper.addNode("examples_trans",myDict["examples_trans"])
    localOper.addNode("tags","未分组")
    localOper.addNode("progress","1")
    localOper.addNum()
    localOper.rewrite()


if ( __name__ == "__main__"):
    path="added_data.xml"
    localOper=LocalOper(path)
    print("*"*40)
    print(" "*5+"欢迎来到查询单词小助手Version 1.0")
    print("*"*40)
    
    while True:
        input_word=input("请输入一个单词,或者输入q退出:")
        if input_word=='q':
            break
        index=localOper.getWordNum(input_word)
        if(index<0):
            #创建词典类 搜索输入的单词
            dictClass=makeDict(input_word)
            #将信息存入字典中
            if(storeToDict(dictClass)==-1):
                continue    #存储失败

            myDict=dictClass.getDict() #存储成功获得字典
            writeLocal(localOper,myDict) #写入本地文件
            localOper=LocalOper(path)   #因为文件更新 所以要重新获取文件信息
            index=localOper.getWordNum(input_word) #在本地文件中查找单词
        localOper.printWordMessage(index)   #输出单词信息
    print("See You Next Time !")
