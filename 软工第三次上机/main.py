#!/usr/bin/python
# -*- coding: utf-8 -*-
from storage import LocalWrite
from search import makeDict
from outPut import Output


def storeToDict(myDict):
    myDict.storeTransToDict()
    myDict.storePhoneticToDict()
    myDict.storeExamplesToDict()
    
if ( __name__ == "__main__"):
    path="added_data.xml"
    output=Output(path)
    input_word=input("请输入一个单词,或者输入q退出:")
    index=output.findWord(input_word)
    if(index<0):
        myDict=makeDict(input_word)
        storeToDict(myDict)
        LocalWrite.rewrite(myDict.getDict(),path)
        output=Output(path)
        output.findWord(input_word)
    output.Output(index)
