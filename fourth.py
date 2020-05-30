#!/usr/bin/python
# -*- coding: utf-8 -*-
from first import Storage
from second import GetNewWord
from fifth import Find
if ( __name__ == "__main__"):
    find=Find("added_data.xml")
    input_word=input("请输入一个单词,或者输入q退出:")
    index=find.findWord(input_word)
    if(index<0):
        word=GetNewWord(input_word)
        word.storeTrans()
        word.storePhonetic()
        word.storeExamples()
        dic=word.getDict()
        Storage.rewrite(dic)
        find=Find("added_data.xml")
        index=find.findWord(input_word)
    find.Output(index)
