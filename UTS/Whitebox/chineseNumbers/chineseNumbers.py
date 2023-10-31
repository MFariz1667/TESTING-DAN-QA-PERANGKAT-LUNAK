#!/usr/bin/env python3

chineseNumChars = {
    1 : "\u4e00",  # in a web page &#x4e00;
    2 : "\u4e8c",
    3 : "\u4e09",
    4 : "\u56db",
    5 : "\u4e94"
}

def printTable():
    for i in range(1,6):
        print(i,chineseNumChars[i])

if __name__=="__main__":
  printTable()
