# -*- coding: cp1251 -*- 
colors = {
    1: "\x1b[01;30m",#�����
    2: "\x1b[01;31m",#����������
    3: "\x1b[01;32m",#�������
    "yellow": "\x1b[01;33m",#������
    "blue": "\x1b[01;34m",#�����
    "magenta": "\x1b[01;35m",
    "cyan": "\x1b[01;36m",
    "white": "\x1b[01;37m",#�����
    "red": "\x1b[01;38m",#�������
    "bold": "\x1b[01;39m"
}

def pain(text, wordcolor):
    for word in text:
        for words in wordcolor:
            if words in word:
                numcolor = wordcolor[words]
            else:
                numcolor = colors["yellow"]
    print(numcolor ,word , end=' ')