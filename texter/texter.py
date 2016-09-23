# -*- coding: cp1251 -*- 
import re
import termocolor
from collections import Counter
from termocolor import pain

soursetext = "text.txt"
soursestop = "stoptext.txt" 
file = open(soursetext)
filestop = open(soursestop)

#������� ���������� 
def delS(my_str): 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in my_str: 
        if char not in punctuations: 
            no_punct = no_punct + char 
    return no_punct 

def filestring(file):
    #���� - ���� ������� ������
    for string in file: 
        smalllist = string.split(" ") 
        words = words + smalllist 
    return wordlist

#��������� ������ ����
def filelist(file):
    #������ ���� ���� � ����� 
    wordlist = [] 
    for string in file: 
        string = delS(string)
        string = re.sub("^\s+|\n|\r|\s+$", '', string)
        if len(string) < 1:
            continue
          
        smalllist = string.split(" ") 
        wordlist = wordlist + smalllist 
    return wordlist

#������� ����-����� �� ������ ����
def stopDEL(wordlist, stoplist):
    count = 0;
    for stop in stoplist:
        for word in wordlist:
            if stop == word:
                count = count + 1
                wordlist.remove(stop)
    print("In this text ", count, " STOP-word")
    return wordlist

wordlist = filelist(file)
stoplist = filelist(filestop)

print("Count of word -> ",len(wordlist)) 
wordlist = stopDEL(wordlist, stoplist)

countword = Counter(wordlist)
for str in countword:
    print(str," -> ",countword[str])

mytext = filestring(file)
pain(mytext, countword)